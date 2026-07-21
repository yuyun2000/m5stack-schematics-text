from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import requests

try:
    from .fetch_schematics import fetch_product
    from .pipeline_common import (
        PROJECT_ROOT,
        load_json,
        load_manifest,
        sha256_bytes,
        sha256_file,
        write_json_if_changed,
    )
    from .publish_descriptions import publish_one
    from .render_description import render_markdown
    from .validate_description import validate_files
except ImportError:
    from fetch_schematics import fetch_product  # type: ignore
    from pipeline_common import (  # type: ignore
        PROJECT_ROOT,
        load_json,
        load_manifest,
        sha256_bytes,
        sha256_file,
        write_json_if_changed,
    )
    from publish_descriptions import publish_one  # type: ignore
    from render_description import render_markdown  # type: ignore
    from validate_description import validate_files  # type: ignore


DEFAULT_BATCH = PROJECT_ROOT / "state" / "description_batch_100.json"
DEFAULT_MANIFEST = PROJECT_ROOT / "state" / "product_manifest.json"
DEFAULT_SCHEMA = PROJECT_ROOT / "schemas" / "schematic-description.schema.json"
ELIGIBLE_ANALYSIS_STATES = {"ready_for_analysis", "facts_invalid"}


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def iso_time(value: datetime) -> str:
    return value.isoformat(timespec="seconds")


def parse_time(value: str) -> datetime:
    parsed = datetime.fromisoformat(value)
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)


def claims_path_for(batch_path: Path) -> Path:
    return batch_path.with_name(f"{batch_path.stem}.claims.json")


def product_snapshot(product: dict[str, Any], ordinal: int) -> dict[str, Any]:
    return {
        "ordinal": ordinal,
        "product_id": product["product_id"],
        "product_name": product["product_name"],
        "output_filename": product["output_filename"],
        "source_path": product["source_path"],
        "source_sha256": product["source_sha256"],
        "input_sha256": product["input_sha256"],
    }


def select_products(
    manifest: dict[str, Any],
    *,
    count: int,
    facts_root: Path,
    published_root: Path,
) -> list[dict[str, Any]]:
    existing_facts = {path.stem for path in facts_root.glob("*.json")}
    candidates = [
        product
        for product in manifest["products"]
        if product["product_id"] not in existing_facts and product.get("schematics")
    ]
    candidates.sort(
        key=lambda product: (
            not (published_root / product["output_filename"]).exists(),
            manifest["products"].index(product),
        )
    )
    if len(candidates) < count:
        raise ValueError(f"Only {len(candidates)} eligible products remain; requested {count}")
    return candidates[:count]


def initialize_batch(
    *,
    batch_path: Path,
    manifest_path: Path,
    count: int,
    batch_id: str,
    facts_root: Path,
    published_root: Path,
) -> tuple[dict[str, Any], bool]:
    manifest = load_manifest(manifest_path)
    products_by_id = {product["product_id"]: product for product in manifest["products"]}
    if batch_path.exists():
        current = load_json(batch_path)
        if current.get("schema_version") != 1:
            raise ValueError(f"Unsupported batch plan: {batch_path}")
        if current.get("target_count") != count:
            raise ValueError(
                f"Existing batch target is {current.get('target_count')}, requested {count}"
            )
        fixed_ids = [item["product_id"] for item in current["products"]]
        if len(fixed_ids) != count or len(set(fixed_ids)) != count:
            raise ValueError("Existing batch does not contain the expected unique product count")
        missing = [product_id for product_id in fixed_ids if product_id not in products_by_id]
        if missing:
            raise ValueError(f"Batch products missing from current manifest: {missing}")
        return current, False
    else:
        selected = select_products(
            manifest,
            count=count,
            facts_root=facts_root,
            published_root=published_root,
        )
        created_at = iso_time(utc_now())
    plan = {
        "schema_version": 1,
        "batch_id": batch_id,
        "created_at": created_at,
        "target_count": count,
        "manifest_sha256": sha256_file(manifest_path),
        "policy": {
            "selection": "missing facts; existing published Markdown first; manifest order",
            "status_source": "derive from assets, facts, Markdown, and per-product report",
            "lease_ttl_minutes": 180,
        },
        "products": [product_snapshot(product, index) for index, product in enumerate(selected, 1)],
    }
    output_names = [item["output_filename"].casefold() for item in plan["products"]]
    if len(set(output_names)) != len(output_names):
        raise ValueError("Batch contains duplicate output filenames")
    changed = write_json_if_changed(batch_path, plan)
    return plan, changed


def load_batch(batch_path: Path) -> dict[str, Any]:
    batch = load_json(batch_path)
    if batch.get("schema_version") != 1 or not isinstance(batch.get("products"), list):
        raise ValueError(f"Unsupported batch plan: {batch_path}")
    if len(batch["products"]) != batch.get("target_count"):
        raise ValueError("Batch product count does not match target_count")
    return batch


def resolve_project_file(root: Path, relative_path: str) -> Path:
    resolved = (root / relative_path).resolve()
    project = root.resolve()
    if resolved != project and project not in resolved.parents:
        raise ValueError(f"Path escapes project root: {relative_path}")
    return resolved


def validate_assets(
    product: dict[str, Any], *, root: Path, assets_root: Path
) -> tuple[str | None, list[str]]:
    manifest_path = assets_root / product["product_id"] / "asset_manifest.json"
    if not manifest_path.exists():
        return "needs_fetch", ["asset_manifest.json is missing"]
    errors: list[str] = []
    try:
        asset_manifest = load_json(manifest_path)
    except Exception as exc:
        return "assets_invalid", [f"asset manifest cannot be parsed: {exc}"]
    if asset_manifest.get("schema_version") != 1:
        errors.append("unsupported asset manifest schema")
    if asset_manifest.get("product_id") != product["product_id"]:
        errors.append("asset manifest product_id mismatch")
    if asset_manifest.get("product_input_sha256") != product["input_sha256"]:
        errors.append("asset manifest is stale for current product input")
    assets = asset_manifest.get("assets")
    if not isinstance(assets, list) or len(assets) != len(product["schematics"]):
        errors.append("asset count does not match product schematics")
        assets = []
    expected_by_ordinal = {item["ordinal"]: item for item in product["schematics"]}
    for asset in assets:
        ordinal = asset.get("ordinal")
        expected = expected_by_ordinal.get(ordinal)
        if not expected or asset.get("source_url") != expected["url"]:
            errors.append(f"asset {ordinal}: source URL mismatch")
        try:
            source = resolve_project_file(root, asset["source_path"])
            if not source.is_file() or sha256_file(source) != asset["sha256"]:
                errors.append(f"asset {ordinal}: source file hash mismatch")
        except Exception as exc:
            errors.append(f"asset {ordinal}: invalid source path: {exc}")
        pages = asset.get("pages")
        if not isinstance(pages, list) or not pages:
            errors.append(f"asset {ordinal}: no rendered pages")
            continue
        for page in pages:
            try:
                page_path = resolve_project_file(root, page["path"])
                if not page_path.is_file() or sha256_file(page_path) != page["sha256"]:
                    errors.append(f"asset {ordinal} page {page.get('page')}: hash mismatch")
            except Exception as exc:
                errors.append(f"asset {ordinal} page {page.get('page')}: invalid path: {exc}")
    return ("assets_invalid", errors) if errors else (None, [])


def valid_publish_report(path: Path, *, product_id: str, digest: str) -> bool:
    if not path.exists():
        return False
    try:
        report = load_json(path)
        results = report["results"]
        return (
            report.get("schema_version") == 1
            and report.get("dry_run") is False
            and report.get("published") == 1
            and report.get("failed") == 0
            and len(results) == 1
            and results[0].get("product_id") == product_id
            and results[0].get("status") == "valid"
            and results[0].get("sha256") == digest
            and not results[0].get("errors")
        )
    except Exception:
        return False


def classify_product(
    product: dict[str, Any],
    *,
    root: Path,
    manifest_path: Path,
    schema_path: Path,
    assets_root: Path,
    facts_root: Path,
    generated_root: Path,
    published_root: Path,
    reports_root: Path,
) -> dict[str, Any]:
    asset_state, asset_errors = validate_assets(product, root=root, assets_root=assets_root)
    if asset_state:
        return {"status": asset_state, "errors": asset_errors}
    facts_path = facts_root / f"{product['product_id']}.json"
    if not facts_path.exists():
        return {"status": "ready_for_analysis", "errors": []}
    try:
        data, validated_product, errors = validate_files(
            facts_path,
            manifest_path=manifest_path,
            asset_manifest_path=assets_root / product["product_id"] / "asset_manifest.json",
            schema_path=schema_path,
        )
    except Exception as exc:
        return {"status": "facts_invalid", "errors": [str(exc)]}
    if errors:
        return {"status": "facts_invalid", "errors": errors}
    markdown = render_markdown(data).encode("utf-8")
    digest = sha256_bytes(markdown)
    draft = generated_root / validated_product["output_filename"]
    published = published_root / validated_product["output_filename"]
    report = reports_root / f"{product['product_id']}-publish.json"
    files_match = (
        draft.exists()
        and published.exists()
        and draft.read_bytes() == markdown
        and published.read_bytes() == markdown
    )
    report_matches = valid_publish_report(
        report, product_id=product["product_id"], digest=digest
    )
    details = {
        "sha256": digest,
        "facts": len(data["facts"]),
        "uncertain": sum(fact["confidence"] == "uncertain" for fact in data["facts"]),
        "needs_review": len(data["needs_review"]),
    }
    if files_match and report_matches:
        return {"status": "complete", "errors": [], **details}
    errors = []
    if not files_match:
        errors.append("generated or published Markdown does not match rendered facts")
    if not report_matches:
        errors.append("per-product publish report is missing or stale")
    return {"status": "ready_to_publish", "errors": errors, **details}


def load_claims(path: Path, *, batch_id: str) -> dict[str, Any]:
    if not path.exists():
        return {"schema_version": 1, "batch_id": batch_id, "leases": {}}
    claims = load_json(path)
    if claims.get("schema_version") != 1 or claims.get("batch_id") != batch_id:
        raise ValueError(f"Claims file does not match batch: {path}")
    if not isinstance(claims.get("leases"), dict):
        raise ValueError(f"Invalid leases in {path}")
    return claims


def batch_status(
    *,
    batch_path: Path,
    manifest_path: Path,
    schema_path: Path,
    root: Path,
    include_claims: bool = True,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    batch = load_batch(batch_path)
    manifest = load_manifest(manifest_path)
    products_by_id = {product["product_id"]: product for product in manifest["products"]}
    claims_path = claims_path_for(batch_path)
    claims = load_claims(claims_path, batch_id=batch["batch_id"])
    now = utc_now()
    details: list[dict[str, Any]] = []
    for item in batch["products"]:
        product = products_by_id.get(item["product_id"])
        if not product:
            result = {"status": "manifest_missing", "errors": ["product missing from manifest"]}
        elif any(
            item[field] != product[field]
            for field in ("product_name", "output_filename", "source_path", "source_sha256", "input_sha256")
        ):
            result = {
                "status": "stale_input",
                "errors": ["current product manifest no longer matches the frozen batch snapshot"],
            }
        else:
            result = classify_product(
                product,
                root=root,
                manifest_path=manifest_path,
                schema_path=schema_path,
                assets_root=root / "artifacts" / "schematics",
                facts_root=root / "artifacts" / "facts",
                generated_root=root / "generated_docs",
                published_root=root / "zh_CN" / "schematic",
                reports_root=root / "reports",
            )
        lease = claims["leases"].get(item["product_id"])
        active_lease = None
        if lease:
            try:
                active_lease = {
                    **lease,
                    "expired": parse_time(lease["expires_at"]) <= now,
                }
            except Exception:
                active_lease = {**lease, "expired": True}
            if result["status"] == "complete":
                active_lease = None
        details.append({**item, **result, "lease": active_lease if include_claims else None})
    counts = Counter(item["status"] for item in details)
    summary = {
        "schema_version": 1,
        "batch_id": batch["batch_id"],
        "target_count": batch["target_count"],
        "counts": dict(sorted(counts.items())),
        "complete": counts["complete"],
        "remaining": batch["target_count"] - counts["complete"],
        "active_leases": sum(item["lease"] is not None for item in details),
    }
    return summary, details


def prune_claims(
    claims: dict[str, Any], details: list[dict[str, Any]], *, now: datetime
) -> bool:
    changed = False
    statuses = {item["product_id"]: item["status"] for item in details}
    for product_id, lease in list(claims["leases"].items()):
        if statuses.get(product_id) == "complete" or product_id not in statuses:
            del claims["leases"][product_id]
            changed = True
    return changed


def claim_next(
    *,
    batch_path: Path,
    manifest_path: Path,
    schema_path: Path,
    root: Path,
    workers: list[str],
    ttl_minutes: int,
) -> list[dict[str, Any]]:
    batch = load_batch(batch_path)
    _, details = batch_status(
        batch_path=batch_path,
        manifest_path=manifest_path,
        schema_path=schema_path,
        root=root,
    )
    claims_path = claims_path_for(batch_path)
    claims = load_claims(claims_path, batch_id=batch["batch_id"])
    now = utc_now()
    prune_claims(claims, details, now=now)
    by_worker = {lease["worker"]: product_id for product_id, lease in claims["leases"].items()}
    eligible = [
        item
        for item in details
        if item["status"] in ELIGIBLE_ANALYSIS_STATES
        and item["product_id"] not in claims["leases"]
    ]
    assignments: list[dict[str, Any]] = []
    for worker in workers:
        product_id = by_worker.get(worker)
        if product_id:
            item = next(item for item in details if item["product_id"] == product_id)
            lease = {
                "worker": worker,
                "claimed_at": claims["leases"][product_id]["claimed_at"],
                "heartbeat_at": iso_time(now),
                "expires_at": iso_time(now + timedelta(minutes=ttl_minutes)),
            }
            claims["leases"][product_id] = lease
            assignments.append({"worker": worker, **item, "lease": lease})
            continue
        if not eligible:
            continue
        item = eligible.pop(0)
        lease = {
            "worker": worker,
            "claimed_at": iso_time(now),
            "heartbeat_at": iso_time(now),
            "expires_at": iso_time(now + timedelta(minutes=ttl_minutes)),
        }
        claims["leases"][item["product_id"]] = lease
        assignments.append({"worker": worker, **item, "lease": lease})
    write_json_if_changed(claims_path, claims)
    return assignments


def release_claim(
    *, batch_path: Path, product_id: str | None, worker: str | None
) -> bool:
    batch = load_batch(batch_path)
    claims_path = claims_path_for(batch_path)
    claims = load_claims(claims_path, batch_id=batch["batch_id"])
    removed = False
    for claimed_id, lease in list(claims["leases"].items()):
        if (product_id and claimed_id == product_id) or (worker and lease["worker"] == worker):
            del claims["leases"][claimed_id]
            removed = True
    if removed:
        write_json_if_changed(claims_path, claims)
    return removed


def fetch_pending(
    *,
    batch_path: Path,
    manifest_path: Path,
    schema_path: Path,
    root: Path,
    limit: int,
    timeout: int,
    max_bytes: int,
    dpi: int,
) -> tuple[int, list[dict[str, str]]]:
    _, details = batch_status(
        batch_path=batch_path,
        manifest_path=manifest_path,
        schema_path=schema_path,
        root=root,
    )
    pending = [item for item in details if item["status"] in {"needs_fetch", "assets_invalid"}]
    if limit > 0:
        pending = pending[:limit]
    manifest = load_manifest(manifest_path)
    products = {product["product_id"]: product for product in manifest["products"]}
    session = requests.Session()
    session.headers.update({"User-Agent": "M5Stack-Schematic-Pipeline/1.0"})
    failures: list[dict[str, str]] = []
    completed = 0
    for item in pending:
        product = products[item["product_id"]]
        try:
            _, changed = fetch_product(
                product,
                assets_root=root / "artifacts" / "schematics",
                session=session,
                timeout=timeout,
                max_bytes=max_bytes,
                dpi=dpi,
            )
            print(f"[{'UPDATED' if changed else 'UNCHANGED'}] {product['product_name']}")
            completed += 1
        except Exception as exc:
            failures.append({"product_id": product["product_id"], "error": str(exc)})
            print(f"[FAIL] {product['product_name']}: {exc}", file=sys.stderr)
    return completed, failures


def publish_ready(
    *,
    batch_path: Path,
    manifest_path: Path,
    schema_path: Path,
    root: Path,
    limit: int,
) -> tuple[int, list[dict[str, Any]]]:
    _, details = batch_status(
        batch_path=batch_path,
        manifest_path=manifest_path,
        schema_path=schema_path,
        root=root,
    )
    pending = [item for item in details if item["status"] == "ready_to_publish"]
    if limit > 0:
        pending = pending[:limit]
    results: list[dict[str, Any]] = []
    for item in pending:
        product_id = item["product_id"]
        try:
            result = publish_one(
                root / "artifacts" / "facts" / f"{product_id}.json",
                manifest_path=manifest_path,
                assets_root=root / "artifacts" / "schematics",
                schema_path=schema_path,
                generated_root=root / "generated_docs",
                published_root=root / "zh_CN" / "schematic",
                backup_root=root / "backups" / "published",
                dry_run=False,
            )
        except Exception as exc:
            result = {"product_id": product_id, "status": "failed", "errors": [str(exc)]}
        report = {
            "schema_version": 1,
            "dry_run": False,
            "published": int(result["status"] == "valid"),
            "failed": int(result["status"] == "failed"),
            "results": [result],
        }
        write_json_if_changed(root / "reports" / f"{product_id}-publish.json", report)
        results.append(result)
        print(json.dumps(result, ensure_ascii=False))
    failures = [result for result in results if result["status"] == "failed"]
    return len(results) - len(failures), failures


def add_common_paths(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Manage an interruption-safe schematic description batch")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init = subparsers.add_parser("init")
    add_common_paths(init)
    init.add_argument("--count", type=int, default=100)
    init.add_argument("--batch-id", default="schematic-rich-100-2026-07-17")

    status = subparsers.add_parser("status")
    add_common_paths(status)
    status.add_argument("--details", action="store_true")

    fetch = subparsers.add_parser("fetch")
    add_common_paths(fetch)
    fetch.add_argument("--limit", type=int, default=0)
    fetch.add_argument("--timeout", type=int, default=60)
    fetch.add_argument("--max-bytes", type=int, default=50 * 1024 * 1024)
    fetch.add_argument("--pdf-dpi", type=int, default=180)

    publish = subparsers.add_parser("publish-ready")
    add_common_paths(publish)
    publish.add_argument("--limit", type=int, default=0)

    claim = subparsers.add_parser("claim-next")
    add_common_paths(claim)
    claim.add_argument("--worker", action="append", required=True)
    claim.add_argument("--ttl-minutes", type=int, default=180)

    release = subparsers.add_parser("release")
    release.add_argument("--batch", type=Path, default=DEFAULT_BATCH)
    release_group = release.add_mutually_exclusive_group(required=True)
    release_group.add_argument("--product-id")
    release_group.add_argument("--worker")

    verify = subparsers.add_parser("verify")
    add_common_paths(verify)
    verify.add_argument("--details", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = PROJECT_ROOT
    if args.command == "init":
        if args.count < 1:
            raise SystemExit("--count must be positive")
        plan, changed = initialize_batch(
            batch_path=args.batch,
            manifest_path=args.manifest,
            count=args.count,
            batch_id=args.batch_id,
            facts_root=root / "artifacts" / "facts",
            published_root=root / "zh_CN" / "schematic",
        )
        print(f"[{'UPDATED' if changed else 'UNCHANGED'}] {args.batch}")
        print(json.dumps({"batch_id": plan["batch_id"], "products": len(plan["products"])}, indent=2))
        return 0
    if args.command == "status":
        summary, details = batch_status(
            batch_path=args.batch,
            manifest_path=args.manifest,
            schema_path=args.schema,
            root=root,
        )
        print(json.dumps({**summary, **({"products": details} if args.details else {})}, ensure_ascii=False, indent=2))
        return 0
    if args.command == "fetch":
        completed, failures = fetch_pending(
            batch_path=args.batch,
            manifest_path=args.manifest,
            schema_path=args.schema,
            root=root,
            limit=args.limit,
            timeout=args.timeout,
            max_bytes=args.max_bytes,
            dpi=args.pdf_dpi,
        )
        print(json.dumps({"fetched": completed, "failures": failures}, ensure_ascii=False, indent=2))
        return 1 if failures else 0
    if args.command == "publish-ready":
        completed, failures = publish_ready(
            batch_path=args.batch,
            manifest_path=args.manifest,
            schema_path=args.schema,
            root=root,
            limit=args.limit,
        )
        print(json.dumps({"published": completed, "failures": failures}, ensure_ascii=False, indent=2))
        return 1 if failures else 0
    if args.command == "claim-next":
        assignments = claim_next(
            batch_path=args.batch,
            manifest_path=args.manifest,
            schema_path=args.schema,
            root=root,
            workers=args.worker,
            ttl_minutes=args.ttl_minutes,
        )
        print(json.dumps({"assignments": assignments}, ensure_ascii=False, indent=2))
        return 0
    if args.command == "release":
        removed = release_claim(
            batch_path=args.batch, product_id=args.product_id, worker=args.worker
        )
        print(f"[{'RELEASED' if removed else 'UNCHANGED'}] {args.product_id or args.worker}")
        return 0
    if args.command == "verify":
        summary, details = batch_status(
            batch_path=args.batch,
            manifest_path=args.manifest,
            schema_path=args.schema,
            root=root,
        )
        print(json.dumps({**summary, **({"products": details} if args.details else {})}, ensure_ascii=False, indent=2))
        return 0 if summary["complete"] == summary["target_count"] else 1
    raise AssertionError(args.command)


if __name__ == "__main__":
    raise SystemExit(main())
