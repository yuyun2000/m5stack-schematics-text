from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

try:
    from .pipeline_common import (
        PROJECT_ROOT,
        load_json,
        sha256_bytes,
        sha256_file,
        write_bytes_if_changed,
        write_json_if_changed,
    )
    from .render_description import render_markdown
    from .validate_description import validate_files
except ImportError:
    from pipeline_common import (  # type: ignore
        PROJECT_ROOT,
        load_json,
        sha256_bytes,
        sha256_file,
        write_bytes_if_changed,
        write_json_if_changed,
    )
    from render_description import render_markdown  # type: ignore
    from validate_description import validate_files  # type: ignore

def backup_existing(path: Path, backup_dir: Path) -> Path | None:
    if not path.exists():
        return None
    digest = sha256_file(path)
    target = backup_dir / f"{digest}.md"
    content = path.read_bytes()
    if sha256_bytes(content) != digest:
        raise RuntimeError(f"Source changed while creating backup: {path}")
    write_bytes_if_changed(target, content)
    if sha256_file(target) != digest:
        raise RuntimeError(f"Backup hash mismatch: {target}")
    return target


def publish_one(
    facts_path: Path,
    *,
    manifest_path: Path,
    assets_root: Path,
    schema_path: Path,
    generated_root: Path,
    published_root: Path,
    backup_root: Path,
    dry_run: bool,
) -> dict[str, Any]:
    try:
        raw = load_json(facts_path)
    except Exception as exc:
        return {"facts": facts_path.as_posix(), "status": "failed", "errors": [str(exc)]}
    product_id = raw.get("product", {}).get("product_id")
    if not product_id:
        return {"facts": facts_path.as_posix(), "status": "failed", "errors": ["missing product_id"]}
    asset_manifest_path = assets_root / product_id / "asset_manifest.json"
    try:
        data, product, errors = validate_files(
            facts_path,
            manifest_path=manifest_path,
            asset_manifest_path=asset_manifest_path,
            schema_path=schema_path,
        )
    except Exception as exc:
        return {"product_id": product_id, "status": "failed", "errors": [str(exc)]}
    if errors:
        return {"product_id": product_id, "status": "failed", "errors": errors}

    markdown = render_markdown(data).encode("utf-8")
    draft = generated_root / product["output_filename"]
    published = published_root / product["output_filename"]
    digest = sha256_bytes(markdown)
    draft_action = "unchanged" if draft.exists() and sha256_file(draft) == digest else "update"
    if not draft.exists():
        draft_action = "create"
    publish_action = "unchanged" if published.exists() and sha256_file(published) == digest else "update"
    if not published.exists():
        publish_action = "create"

    backup = None
    try:
        if not dry_run and publish_action == "update":
            backup = backup_existing(published, backup_root / product_id)
        if not dry_run:
            write_bytes_if_changed(draft, markdown)
            write_bytes_if_changed(published, markdown)
            if sha256_file(draft) != digest or sha256_file(published) != digest:
                raise RuntimeError(f"Post-publish hash mismatch for {product_id}")
    except Exception as exc:
        return {"product_id": product_id, "status": "failed", "errors": [str(exc)]}

    uncertain_facts = sum(fact["confidence"] == "uncertain" for fact in data["facts"])
    return {
        "product_id": product_id,
        "product_name": product["product_name"],
        "status": "valid",
        "dry_run": dry_run,
        "draft_action": draft_action,
        "publish_action": publish_action,
        "sha256": digest,
        "uncertain_facts": uncertain_facts,
        "needs_review": len(data["needs_review"]),
        "backup": backup.as_posix() if backup else None,
        "errors": [],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate, render, and automatically publish schematic descriptions")
    parser.add_argument("--facts", type=Path, action="append", default=[])
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--manifest", type=Path, default=PROJECT_ROOT / "state" / "product_manifest.json")
    parser.add_argument("--assets-root", type=Path, default=PROJECT_ROOT / "artifacts" / "schematics")
    parser.add_argument("--schema", type=Path, default=PROJECT_ROOT / "schemas" / "schematic-description.schema.json")
    parser.add_argument("--generated-root", type=Path, default=PROJECT_ROOT / "generated_docs")
    parser.add_argument("--published-root", type=Path, default=PROJECT_ROOT / "zh_CN" / "schematic")
    parser.add_argument("--backup-root", type=Path, default=PROJECT_ROOT / "backups" / "published")
    parser.add_argument("--report", type=Path, default=PROJECT_ROOT / "reports" / "publish-report.json")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.all == bool(args.facts):
        raise SystemExit("Use --all or one or more --facts")
    facts_files = sorted((PROJECT_ROOT / "artifacts" / "facts").glob("*.json")) if args.all else args.facts
    results = [
        publish_one(
            facts_path,
            manifest_path=args.manifest,
            assets_root=args.assets_root,
            schema_path=args.schema,
            generated_root=args.generated_root,
            published_root=args.published_root,
            backup_root=args.backup_root,
            dry_run=args.dry_run,
        )
        for facts_path in facts_files
    ]
    report = {
        "schema_version": 1,
        "dry_run": args.dry_run,
        "published": sum(item["status"] == "valid" for item in results),
        "failed": sum(item["status"] == "failed" for item in results),
        "results": results,
    }
    write_json_if_changed(args.report, report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
