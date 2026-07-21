from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

import jsonschema

try:
    from .pipeline_common import PROJECT_ROOT, find_product, load_json, load_manifest, write_json_if_changed
except ImportError:
    from pipeline_common import PROJECT_ROOT, find_product, load_json, load_manifest, write_json_if_changed  # type: ignore


SPECULATIVE_MARKERS = ("可能", "通常", "一般", "大概", "推测", "疑似", "typically", "probably", "likely")


def validate_description_data(
    data: dict[str, Any],
    *,
    schema: dict[str, Any],
    product: dict[str, Any],
    asset_manifest: dict[str, Any],
) -> list[str]:
    errors: list[str] = []
    validator = jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker())
    for error in sorted(validator.iter_errors(data), key=lambda item: list(item.path)):
        location = "/".join(str(part) for part in error.path) or "<root>"
        errors.append(f"schema:{location}: {error.message}")
    if errors:
        return errors

    expected_product = {
        key: product[key]
        for key in ("product_id", "product_name", "sku", "source_path", "source_sha256", "input_sha256")
    }
    if data["product"] != expected_product:
        errors.append("product metadata does not match product_manifest.json")

    expected_assets = [
        {
            "sha256": asset["sha256"],
            "source_url": asset["source_url"],
            "pages": [page["page"] for page in asset["pages"]],
        }
        for asset in asset_manifest["assets"]
    ]
    if data["schematic_assets"] != expected_assets:
        errors.append("schematic_assets do not match asset_manifest.json")

    asset_pages = {
        asset["sha256"]: {page["page"] for page in asset["pages"]}
        for asset in asset_manifest["assets"]
    }

    def check_evidence(evidence: list[dict[str, Any]], owner: str) -> None:
        for item in evidence:
            digest = item["asset_sha256"]
            if digest not in asset_pages:
                errors.append(f"{owner}: unknown evidence asset {digest}")
            elif item["page"] not in asset_pages[digest]:
                errors.append(f"{owner}: invalid evidence page {item['page']} for asset {digest}")

    ids: set[str] = set()
    uncertain_ids: set[str] = set()
    for component in data["components"]:
        check_evidence(component["evidence"], f"component:{component['reference']}")
    for fact in data["facts"]:
        fact_id = fact["id"]
        if fact_id in ids:
            errors.append(f"duplicate fact id: {fact_id}")
        ids.add(fact_id)
        check_evidence(fact["evidence"], f"fact:{fact_id}")
        if fact["confidence"] == "confirmed":
            lowered = fact["statement"].casefold()
            markers = [marker for marker in SPECULATIVE_MARKERS if marker.casefold() in lowered]
            if markers:
                errors.append(f"fact:{fact_id}: confirmed statement contains speculative marker {markers[0]!r}")
        else:
            uncertain_ids.add(fact_id)

    review_ids: set[str] = set()
    reviewed_fact_ids: set[str] = set()
    for item in data["needs_review"]:
        if item["id"] in review_ids:
            errors.append(f"duplicate needs_review id: {item['id']}")
        review_ids.add(item["id"])
        if item["fact_id"] is not None:
            reviewed_fact_ids.add(item["fact_id"])
            if item["fact_id"] not in ids:
                errors.append(f"needs_review:{item['id']}: unknown fact_id {item['fact_id']}")
        check_evidence(item["evidence"], f"needs_review:{item['id']}")
    for fact_id in sorted(uncertain_ids - reviewed_fact_ids):
        errors.append(f"uncertain fact lacks needs_review entry: {fact_id}")
    return errors


def validate_files(
    facts_path: Path,
    *,
    manifest_path: Path,
    asset_manifest_path: Path,
    schema_path: Path,
) -> tuple[dict[str, Any], dict[str, Any], list[str]]:
    data = load_json(facts_path)
    manifest = load_manifest(manifest_path)
    product_id = data.get("product", {}).get("product_id")
    product = find_product(manifest, product_id=product_id)
    asset_manifest = load_json(asset_manifest_path)
    schema = load_json(schema_path)
    errors = validate_description_data(
        data,
        schema=schema,
        product=product,
        asset_manifest=asset_manifest,
    )
    return data, product, errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate structured schematic facts")
    parser.add_argument("facts", type=Path)
    parser.add_argument("--manifest", type=Path, default=PROJECT_ROOT / "state" / "product_manifest.json")
    parser.add_argument("--assets-root", type=Path, default=PROJECT_ROOT / "artifacts" / "schematics")
    parser.add_argument("--schema", type=Path, default=PROJECT_ROOT / "schemas" / "schematic-description.schema.json")
    parser.add_argument("--report", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    data = load_json(args.facts)
    product_id = data.get("product", {}).get("product_id")
    if not product_id or not re.fullmatch(r"[A-Za-z0-9._-]+", product_id):
        print("[FAIL] facts file has no valid product_id", file=sys.stderr)
        return 1
    asset_manifest_path = args.assets_root / product_id / "asset_manifest.json"
    _, product, errors = validate_files(
        args.facts,
        manifest_path=args.manifest,
        asset_manifest_path=asset_manifest_path,
        schema_path=args.schema,
    )
    report = {
        "schema_version": 1,
        "product_id": product_id,
        "product_name": product["product_name"],
        "valid": not errors,
        "errors": errors,
    }
    if args.report:
        write_json_if_changed(args.report, report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
