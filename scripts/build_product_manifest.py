from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

try:
    from .pipeline_common import (
        PROJECT_ROOT,
        canonical_json_bytes,
        sanitize_output_stem,
        sha256_bytes,
        sha256_file,
        stable_product_id,
        write_json_if_changed,
    )
except ImportError:
    from pipeline_common import (  # type: ignore
        PROJECT_ROOT,
        canonical_json_bytes,
        sanitize_output_stem,
        sha256_bytes,
        sha256_file,
        stable_product_id,
        write_json_if_changed,
    )


REMOVED_TAGS = (
    "TabPanel",
    "video",
    "PictureViewer",
    "VideoPlayer",
    "IframePlayer",
    "Script",
    "style",
    "SchViewer",
)
IMAGE_EXTENSIONS = ("webp", "png", "jpg", "jpeg", "gif")


def clean_content(content: str) -> str:
    cleaned = content
    for tag in REMOVED_TAGS:
        pattern = rf"<{tag}\b[^>]*>.*?</{tag}\s*>"
        cleaned = re.sub(pattern, "", cleaned, flags=re.IGNORECASE | re.DOTALL)
    return re.sub(r"\n{3,}", "\n\n", cleaned).strip()


def extract_product_name(content: str) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", content, re.MULTILINE)
    return match.group(1).strip() if match else "Unknown"


def extract_sku(content: str) -> str | None:
    match = re.search(r"\bSKU\s*[:：]\s*([A-Za-z0-9._-]+)", content, re.IGNORECASE)
    return match.group(1) if match else None


def extract_schematic_urls(content: str) -> list[dict[str, Any]]:
    section_match = re.search(
        r"^##[ \t]+原理图[^\r\n]*\r?\n(.*?)(?=^##[ \t]+|\Z)",
        content,
        re.MULTILINE | re.DOTALL,
    )
    if not section_match:
        return []
    section = section_match.group(1)
    extension_pattern = "|".join(IMAGE_EXTENSIONS)
    image_patterns = (
        rf'<img\b[^>]*\bsrc\s*=\s*["\'](https?://[^"\']+\.(?:{extension_pattern})(?:\?[^"\']*)?)["\']',
        rf'!\[[^\]]*\]\((https?://[^)\s]+\.(?:{extension_pattern})(?:\?[^)\s]*)?)\)',
    )
    image_urls: list[str] = []
    for pattern in image_patterns:
        image_urls.extend(re.findall(pattern, section, flags=re.IGNORECASE))
    if image_urls:
        urls = list(dict.fromkeys(image_urls))
        return [{"ordinal": index, "kind": "image", "url": url} for index, url in enumerate(urls)]

    pdf_urls = re.findall(
        r"\[[^\]]*\]\((https?://[^)\s]+\.pdf(?:\?[^)\s]*)?)\)",
        section,
        flags=re.IGNORECASE,
    )
    urls = list(dict.fromkeys(pdf_urls))
    return [{"ordinal": index, "kind": "pdf", "url": url} for index, url in enumerate(urls)]


def iter_source_files(source_root: Path) -> Iterable[Path]:
    published_root = (source_root / "schematic").resolve()
    for path in sorted(source_root.rglob("*.md"), key=lambda item: item.as_posix().casefold()):
        resolved = path.resolve()
        if published_root == resolved or published_root in resolved.parents:
            continue
        yield path


def build_manifest(source_root: Path) -> dict[str, Any]:
    source_root = source_root.resolve()
    products: list[dict[str, Any]] = []
    for source_file in iter_source_files(source_root):
        raw = source_file.read_text(encoding="utf-8")
        schematics = extract_schematic_urls(raw)
        if not schematics:
            continue
        relative_path = source_file.relative_to(source_root).as_posix()
        extracted_name = extract_product_name(raw)
        title_missing = extracted_name == "Unknown"
        product_name = source_file.stem if title_missing else extracted_name
        cleaned = clean_content(raw)
        product_id = stable_product_id(product_name, relative_path)
        input_fingerprint = {
            "product_name": product_name,
            "source_sha256": sha256_file(source_file),
            "schematics": schematics,
        }
        products.append(
            {
                "product_id": product_id,
                "product_name": product_name,
                "title_missing": title_missing,
                "sku": extract_sku(raw),
                "source_path": relative_path,
                "source_sha256": input_fingerprint["source_sha256"],
                "input_sha256": sha256_bytes(canonical_json_bytes(input_fingerprint)),
                "output_filename": f"{sanitize_output_stem(product_name)}.md",
                "schematics": schematics,
                "document_content": cleaned,
            }
        )

    products.sort(key=lambda item: (item["source_path"].casefold(), item["product_id"]))
    stem_counts = Counter(item["output_filename"].casefold() for item in products)
    for item in products:
        if stem_counts[item["output_filename"].casefold()] > 1:
            stem = Path(item["output_filename"]).stem
            item["output_filename"] = f"{stem}--{item['product_id'][-8:]}.md"

    image_products = sum(any(s["kind"] == "image" for s in p["schematics"]) for p in products)
    pdf_products = sum(all(s["kind"] == "pdf" for s in p["schematics"]) for p in products)
    duplicate_names = sorted(
        name for name, count in Counter(item["product_name"] for item in products).items() if count > 1
    )
    missing_titles = [item["source_path"] for item in products if item["title_missing"]]
    return {
        "schema_version": 1,
        "source_root": source_root.name,
        "summary": {
            "products": len(products),
            "image_products": image_products,
            "pdf_only_products": pdf_products,
            "duplicate_product_names": duplicate_names,
            "missing_product_titles": missing_titles,
        },
        "products": products,
    }


def write_legacy_csv(path: Path, products: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.writer(handle)
        writer.writerow(["产品名", "原理图地址", "文档内容"])
        for product in products:
            urls = ",".join(item["url"] for item in product["schematics"])
            writer.writerow([product["product_name"], urls, product["document_content"]])


def write_legacy_xlsx(path: Path, products: list[dict[str, Any]]) -> None:
    try:
        import openpyxl
        from openpyxl.styles import Alignment, Font
    except ImportError as exc:
        raise RuntimeError("openpyxl is required for XLSX export") from exc

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "原理图产品"
    sheet.append(["产品名", "原理图地址", "文档内容"])
    for cell in sheet[1]:
        cell.font = Font(bold=True)
        cell.alignment = Alignment(horizontal="center", vertical="center")
    for product in products:
        urls = ",".join(item["url"] for item in product["schematics"])
        sheet.append([product["product_name"], urls, product["document_content"]])
    sheet.column_dimensions["A"].width = 30
    sheet.column_dimensions["B"].width = 50
    sheet.column_dimensions["C"].width = 100
    for row in sheet.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = Alignment(wrap_text=True, vertical="top")
    path.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the deterministic schematic product manifest")
    parser.add_argument("--source-root", type=Path, default=PROJECT_ROOT / "zh_CN")
    parser.add_argument("--manifest", type=Path, default=PROJECT_ROOT / "state" / "product_manifest.json")
    parser.add_argument("--csv", type=Path, default=PROJECT_ROOT / "schematic_products.csv")
    parser.add_argument("--xlsx", type=Path, default=PROJECT_ROOT / "schematic_products.xlsx")
    parser.add_argument("--no-legacy-exports", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest = build_manifest(args.source_root)
    summary = manifest["summary"]
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if args.dry_run:
        return 0
    changed = write_json_if_changed(args.manifest, manifest)
    print(f"[{'UPDATED' if changed else 'UNCHANGED'}] {args.manifest}")
    if not args.no_legacy_exports:
        write_legacy_csv(args.csv, manifest["products"])
        write_legacy_xlsx(args.xlsx, manifest["products"])
        print(f"[UPDATED] {args.csv}")
        print(f"[UPDATED] {args.xlsx}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
