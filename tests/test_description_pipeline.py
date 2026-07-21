from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.pipeline_common import sha256_file
from scripts.publish_descriptions import publish_one
from scripts.render_description import render_markdown
from scripts.validate_description import validate_description_data


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def fixture_data() -> tuple[dict, dict, dict]:
    digest = "a" * 64
    source_digest = "b" * 64
    input_digest = "c" * 64
    product = {
        "product_id": "demo-123456789abc",
        "product_name": "Demo",
        "sku": "U001",
        "source_path": "unit/demo.md",
        "source_sha256": source_digest,
        "input_sha256": input_digest,
        "output_filename": "Demo.md",
    }
    asset_manifest = {
        "schema_version": 1,
        "product_id": product["product_id"],
        "product_name": product["product_name"],
        "product_input_sha256": input_digest,
        "assets_sha256": "d" * 64,
        "fetched_at": "2026-07-17T00:00:00+00:00",
        "assets": [
            {
                "ordinal": 0,
                "kind": "image",
                "source_url": "https://example.test/demo.webp",
                "source_path": "artifacts/schematics/demo/source_001.webp",
                "sha256": digest,
                "bytes": 12,
                "content_type": "image/webp",
                "pages": [
                    {
                        "page": 1,
                        "path": "artifacts/schematics/demo/source_001.webp",
                        "sha256": digest,
                    }
                ],
            }
        ],
    }
    evidence = [{"asset_sha256": digest, "page": 1, "locator": "U1 and NET_A"}]
    data = {
        "schema_version": 1,
        "generator": "schematic_describer",
        "product": {key: product[key] for key in ("product_id", "product_name", "sku", "source_path", "source_sha256", "input_sha256")},
        "schematic_assets": [
            {
                "sha256": digest,
                "source_url": "https://example.test/demo.webp",
                "pages": [1],
            }
        ],
        "summary": "Demo board uses U1 to connect the documented interface.",
        "keywords": ["Demo", "U001", "ABC123"],
        "components": [
            {"reference": "U1", "part_number": "ABC123", "role": "Controller", "evidence": evidence}
        ],
        "facts": [
            {
                "id": "component.u1",
                "category": "component",
                "subject": "U1",
                "statement": "U1 is marked ABC123 and connects to NET_A.",
                "confidence": "confirmed",
                "attributes": {"part_number": "ABC123"},
                "evidence": evidence,
            }
        ],
        "needs_review": [],
    }
    return product, asset_manifest, data


class DescriptionPipelineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fact_schema = json.loads(
            (PROJECT_ROOT / "schemas" / "schematic-description.schema.json").read_text(encoding="utf-8")
        )

    def test_valid_facts_and_markdown_render(self) -> None:
        product, asset_manifest, data = fixture_data()
        errors = validate_description_data(
            data, schema=self.fact_schema, product=product, asset_manifest=asset_manifest
        )
        self.assertEqual(errors, [])
        markdown = render_markdown(data)
        self.assertIn("# Demo 原理图描述", markdown)
        self.assertIn("U1 is marked ABC123", markdown)
        self.assertIn("## 待确认事项", markdown)
        self.assertIn("没有标记为 `uncertain`", markdown)
        self.assertIn("## 原理图来源", markdown)
        self.assertIn("https://example.test/demo.webp", markdown)
        self.assertIn("`" + "a" * 64 + "`", markdown)
        self.assertIn("源文档 SHA-256", markdown)

    def test_confirmed_fact_rejects_speculative_language(self) -> None:
        product, asset_manifest, data = fixture_data()
        data["facts"][0]["statement"] = "U1 可能连接到 NET_A。"
        errors = validate_description_data(
            data, schema=self.fact_schema, product=product, asset_manifest=asset_manifest
        )
        self.assertTrue(any("speculative marker" in error for error in errors))

    def test_uncertain_fact_requires_review_link(self) -> None:
        product, asset_manifest, data = fixture_data()
        data["facts"][0]["confidence"] = "uncertain"
        errors = validate_description_data(
            data, schema=self.fact_schema, product=product, asset_manifest=asset_manifest
        )
        self.assertTrue(any("lacks needs_review" in error for error in errors))

    def test_publish_is_automatic_and_backs_up_changed_document(self) -> None:
        product, asset_manifest, data = fixture_data()
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest_path = root / "product_manifest.json"
            manifest = {"schema_version": 1, "products": [product]}
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            generated = root / "generated"
            published = root / "published"
            facts_root = root / "facts"
            assets_root = root / "assets"
            generated.mkdir()
            facts_root.mkdir()
            (assets_root / product["product_id"]).mkdir(parents=True)
            draft = generated / product["output_filename"]
            draft.write_text(render_markdown(data), encoding="utf-8")
            (facts_root / f"{product['product_id']}.json").write_text(
                json.dumps(data), encoding="utf-8"
            )
            (assets_root / product["product_id"] / "asset_manifest.json").write_text(
                json.dumps(asset_manifest), encoding="utf-8"
            )
            published.mkdir()
            old_published = published / product["output_filename"]
            old_published.write_text("old content", encoding="utf-8")
            old_hash = sha256_file(old_published)
            result = publish_one(
                facts_root / f"{product['product_id']}.json",
                manifest_path=manifest_path,
                assets_root=assets_root,
                schema_path=PROJECT_ROOT / "schemas" / "schematic-description.schema.json",
                generated_root=generated,
                published_root=published,
                backup_root=root / "backups",
                dry_run=False,
            )
            self.assertEqual(result["status"], "valid")
            self.assertEqual(result["publish_action"], "update")
            self.assertEqual(sha256_file(old_published), result["sha256"])
            self.assertTrue((root / "backups" / product["product_id"] / f"{old_hash}.md").exists())


if __name__ == "__main__":
    unittest.main()
