from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.manage_description_batch import (
    batch_status,
    claim_next,
    initialize_batch,
    publish_ready,
    release_claim,
    select_products,
)
from scripts.pipeline_common import sha256_bytes, write_bytes_if_changed, write_json_if_changed
from scripts.publish_descriptions import publish_one


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def product(product_id: str, name: str, output_filename: str) -> dict:
    marker = product_id[0]
    return {
        "product_id": product_id,
        "product_name": name,
        "sku": "T001",
        "source_path": f"unit/{product_id}.md",
        "source_sha256": marker * 64,
        "input_sha256": marker * 64,
        "output_filename": output_filename,
        "schematics": [
            {
                "ordinal": 0,
                "kind": "image",
                "url": f"https://example.test/{product_id}.png",
            }
        ],
    }


class BatchManagerTests(unittest.TestCase):
    def test_atomic_write_is_idempotent_and_leaves_no_temporary_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "state.json"
            self.assertTrue(write_bytes_if_changed(path, b"first"))
            self.assertFalse(write_bytes_if_changed(path, b"first"))
            self.assertTrue(write_bytes_if_changed(path, b"second"))
            self.assertEqual(path.read_bytes(), b"second")
            self.assertEqual(list(path.parent.glob(f".{path.name}.*.tmp")), [])

    def test_selection_prefers_published_and_excludes_existing_facts(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            facts = root / "facts"
            published = root / "published"
            facts.mkdir()
            published.mkdir()
            products = [
                product("alpha-11111111", "Alpha", "Alpha.md"),
                product("bravo-22222222", "Bravo", "Bravo.md"),
                product("charlie-33333333", "Charlie", "Charlie.md"),
            ]
            (published / "Bravo.md").write_text("legacy", encoding="utf-8")
            (facts / "charlie-33333333.json").write_text("{}", encoding="utf-8")
            selected = select_products(
                {"schema_version": 1, "products": products},
                count=2,
                facts_root=facts,
                published_root=published,
            )
            self.assertEqual([item["product_id"] for item in selected], ["bravo-22222222", "alpha-11111111"])

    def test_second_batch_excludes_products_completed_by_first_batch(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest_path = root / "manifest.json"
            facts = root / "facts"
            published = root / "published"
            facts.mkdir()
            published.mkdir()
            products = [
                product("alpha-11111111", "Alpha", "Alpha.md"),
                product("bravo-22222222", "Bravo", "Bravo.md"),
                product("charlie-33333333", "Charlie", "Charlie.md"),
                product("delta-44444444", "Delta", "Delta.md"),
            ]
            write_json_if_changed(manifest_path, {"schema_version": 1, "products": products})
            first, _ = initialize_batch(
                batch_path=root / "batch_2.json",
                manifest_path=manifest_path,
                count=2,
                batch_id="first-batch",
                facts_root=facts,
                published_root=published,
            )
            for item in first["products"]:
                (facts / f"{item['product_id']}.json").write_text("{}", encoding="utf-8")

            second, _ = initialize_batch(
                batch_path=root / "next_batch_2.json",
                manifest_path=manifest_path,
                count=2,
                batch_id="second-batch",
                facts_root=facts,
                published_root=published,
            )

            first_ids = {item["product_id"] for item in first["products"]}
            second_ids = {item["product_id"] for item in second["products"]}
            self.assertEqual(first_ids, {"alpha-11111111", "bravo-22222222"})
            self.assertEqual(second_ids, {"charlie-33333333", "delta-44444444"})
            self.assertFalse(first_ids & second_ids)

    def test_existing_batch_keeps_product_ids_when_manifest_order_changes(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest_path = root / "manifest.json"
            batch_path = root / "batch.json"
            facts = root / "facts"
            published = root / "published"
            facts.mkdir()
            published.mkdir()
            products = [
                product("alpha-11111111", "Alpha", "Alpha.md"),
                product("bravo-22222222", "Bravo", "Bravo.md"),
            ]
            write_json_if_changed(manifest_path, {"schema_version": 1, "products": products})
            first, _ = initialize_batch(
                batch_path=batch_path,
                manifest_path=manifest_path,
                count=1,
                batch_id="test-batch",
                facts_root=facts,
                published_root=published,
            )
            write_json_if_changed(manifest_path, {"schema_version": 1, "products": list(reversed(products))})
            second, _ = initialize_batch(
                batch_path=batch_path,
                manifest_path=manifest_path,
                count=1,
                batch_id="ignored-on-resume",
                facts_root=facts,
                published_root=published,
            )
            self.assertEqual(first["products"][0]["product_id"], second["products"][0]["product_id"])
            self.assertEqual(second["batch_id"], "test-batch")

    def test_existing_batch_reports_stale_input_instead_of_rebasing(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest_path = root / "manifest.json"
            batch_path = root / "batch.json"
            (root / "facts").mkdir()
            (root / "published").mkdir()
            current = product("alpha-aaaaaaaa", "Alpha", "Alpha.md")
            write_json_if_changed(manifest_path, {"schema_version": 1, "products": [current]})
            initialize_batch(
                batch_path=batch_path,
                manifest_path=manifest_path,
                count=1,
                batch_id="stale-test",
                facts_root=root / "facts",
                published_root=root / "published",
            )
            changed = {**current, "input_sha256": "f" * 64}
            write_json_if_changed(manifest_path, {"schema_version": 1, "products": [changed]})
            for relative in ("artifacts/facts", "artifacts/schematics", "generated_docs", "zh_CN/schematic", "reports"):
                (root / relative).mkdir(parents=True, exist_ok=True)
            summary, _ = batch_status(
                batch_path=batch_path,
                manifest_path=manifest_path,
                schema_path=PROJECT_ROOT / "schemas" / "schematic-description.schema.json",
                root=root,
            )
            self.assertEqual(summary["counts"], {"stale_input": 1})

    def test_corrupt_facts_return_single_product_failure(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            facts_path = root / "broken.json"
            facts_path.write_text("{", encoding="utf-8")
            result = publish_one(
                facts_path,
                manifest_path=root / "manifest.json",
                assets_root=root / "assets",
                schema_path=PROJECT_ROOT / "schemas" / "schematic-description.schema.json",
                generated_root=root / "generated",
                published_root=root / "published",
                backup_root=root / "backups",
                dry_run=False,
            )
            self.assertEqual(result["status"], "failed")
            self.assertTrue(result["errors"])

    def test_status_claim_publish_and_resume_cycle(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest_path = root / "manifest.json"
            schema_path = PROJECT_ROOT / "schemas" / "schematic-description.schema.json"
            batch_path = root / "batch.json"
            for relative in (
                "artifacts/facts",
                "artifacts/schematics",
                "generated_docs",
                "zh_CN/schematic",
                "reports",
                "backups/published",
            ):
                (root / relative).mkdir(parents=True)
            current = product("demo-44444444", "Demo", "Demo.md")
            (root / "zh_CN" / "schematic" / "Demo.md").write_text("legacy", encoding="utf-8")
            write_json_if_changed(manifest_path, {"schema_version": 1, "products": [current]})
            initialize_batch(
                batch_path=batch_path,
                manifest_path=manifest_path,
                count=1,
                batch_id="test-cycle",
                facts_root=root / "artifacts" / "facts",
                published_root=root / "zh_CN" / "schematic",
            )
            summary, _ = batch_status(
                batch_path=batch_path,
                manifest_path=manifest_path,
                schema_path=schema_path,
                root=root,
            )
            self.assertEqual(summary["counts"], {"needs_fetch": 1})

            source = root / "artifacts" / "schematics" / current["product_id"] / "source_001.png"
            source.parent.mkdir(parents=True)
            source.write_bytes(b"schematic bytes")
            digest = sha256_bytes(source.read_bytes())
            asset_manifest = {
                "schema_version": 1,
                "product_id": current["product_id"],
                "product_name": current["product_name"],
                "product_input_sha256": current["input_sha256"],
                "assets_sha256": "f" * 64,
                "fetched_at": "2026-07-17T00:00:00+00:00",
                "assets": [
                    {
                        "ordinal": 0,
                        "kind": "image",
                        "source_url": current["schematics"][0]["url"],
                        "source_path": source.relative_to(root).as_posix(),
                        "sha256": digest,
                        "bytes": source.stat().st_size,
                        "content_type": "image/png",
                        "pages": [
                            {"page": 1, "path": source.relative_to(root).as_posix(), "sha256": digest}
                        ],
                    }
                ],
            }
            write_json_if_changed(source.parent / "asset_manifest.json", asset_manifest)
            assignments = claim_next(
                batch_path=batch_path,
                manifest_path=manifest_path,
                schema_path=schema_path,
                root=root,
                workers=["worker-1"],
                ttl_minutes=30,
            )
            self.assertEqual(assignments[0]["product_id"], current["product_id"])
            repeated = claim_next(
                batch_path=batch_path,
                manifest_path=manifest_path,
                schema_path=schema_path,
                root=root,
                workers=["worker-1"],
                ttl_minutes=30,
            )
            self.assertEqual(repeated[0]["product_id"], current["product_id"])
            self.assertTrue(release_claim(batch_path=batch_path, product_id=None, worker="worker-1"))

            facts = {
                "schema_version": 1,
                "generator": "schematic_describer",
                "product": {
                    key: current[key]
                    for key in ("product_id", "product_name", "sku", "source_path", "source_sha256", "input_sha256")
                },
                "schematic_assets": [
                    {"sha256": digest, "source_url": current["schematics"][0]["url"], "pages": [1]}
                ],
                "summary": "Demo board has a documented U1 controller and a NET_A interface connection.",
                "keywords": ["Demo", "U1", "NET_A"],
                "components": [
                    {
                        "reference": "U1",
                        "part_number": "DEMO1",
                        "role": "controller",
                        "evidence": [{"asset_sha256": digest, "page": 1, "locator": "U1 area"}],
                    }
                ],
                "facts": [
                    {
                        "id": "component.u1",
                        "category": "component",
                        "subject": "U1",
                        "statement": "U1 is marked DEMO1 and connects to NET_A.",
                        "confidence": "confirmed",
                        "attributes": {"net": "NET_A"},
                        "evidence": [{"asset_sha256": digest, "page": 1, "locator": "U1 area"}],
                    }
                ],
                "needs_review": [],
            }
            write_json_if_changed(root / "artifacts" / "facts" / f"{current['product_id']}.json", facts)
            summary, _ = batch_status(
                batch_path=batch_path,
                manifest_path=manifest_path,
                schema_path=schema_path,
                root=root,
            )
            self.assertEqual(summary["counts"], {"ready_to_publish": 1})
            completed, failures = publish_ready(
                batch_path=batch_path,
                manifest_path=manifest_path,
                schema_path=schema_path,
                root=root,
                limit=0,
            )
            self.assertEqual((completed, failures), (1, []))
            summary, _ = batch_status(
                batch_path=batch_path,
                manifest_path=manifest_path,
                schema_path=schema_path,
                root=root,
            )
            self.assertEqual(summary["counts"], {"complete": 1})


if __name__ == "__main__":
    unittest.main()
