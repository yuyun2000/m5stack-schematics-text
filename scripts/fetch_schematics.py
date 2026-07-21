from __future__ import annotations

import argparse
import json
import mimetypes
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

import requests

try:
    from .pipeline_common import (
        PROJECT_ROOT,
        canonical_json_bytes,
        find_product,
        load_json,
        load_manifest,
        sha256_bytes,
        sha256_file,
        write_bytes_if_changed,
        write_json_if_changed,
    )
except ImportError:
    from pipeline_common import (  # type: ignore
        PROJECT_ROOT,
        canonical_json_bytes,
        find_product,
        load_json,
        load_manifest,
        sha256_bytes,
        sha256_file,
        write_bytes_if_changed,
        write_json_if_changed,
    )


CONTENT_TYPE_EXTENSIONS = {
    "application/pdf": ".pdf",
    "image/gif": ".gif",
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/webp": ".webp",
}
SUPPORTED_EXTENSIONS = {".pdf", ".gif", ".jpeg", ".jpg", ".png", ".webp"}


def safe_log_url(url: str) -> str:
    parsed = urlsplit(url)
    return parsed._replace(query="", fragment="").geturl()


def choose_extension(url: str, content_type: str | None) -> str:
    suffix = Path(urlsplit(url).path).suffix.lower()
    if suffix in SUPPORTED_EXTENSIONS:
        return ".jpg" if suffix == ".jpeg" else suffix
    normalized_type = (content_type or "").split(";", 1)[0].strip().lower()
    extension = CONTENT_TYPE_EXTENSIONS.get(normalized_type)
    if extension:
        return extension
    guessed = mimetypes.guess_extension(normalized_type) if normalized_type else None
    if guessed in SUPPORTED_EXTENSIONS:
        return ".jpg" if guessed == ".jpeg" else guessed
    raise ValueError(f"Unsupported schematic content type: {content_type!r}")


def detect_extension(data: bytes) -> str:
    if data.startswith(b"%PDF-"):
        return ".pdf"
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        return ".png"
    if data.startswith(b"\xff\xd8\xff"):
        return ".jpg"
    if data.startswith((b"GIF87a", b"GIF89a")):
        return ".gif"
    if data.startswith(b"RIFF") and len(data) >= 12 and data[8:12] == b"WEBP":
        return ".webp"
    raise ValueError("Downloaded content is not a supported image or PDF")


def validate_magic(data: bytes, extension: str) -> None:
    actual = detect_extension(data)
    if actual != extension:
        raise ValueError(f"Downloaded content is {actual}, not {extension}")


def download_bytes(session: requests.Session, url: str, timeout: int, max_bytes: int) -> tuple[bytes, str]:
    with session.get(url, stream=True, timeout=(10, timeout)) as response:
        response.raise_for_status()
        content_type = response.headers.get("Content-Type", "")
        chunks: list[bytes] = []
        total = 0
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if not chunk:
                continue
            total += len(chunk)
            if total > max_bytes:
                raise ValueError(f"Schematic exceeds maximum size of {max_bytes} bytes")
            chunks.append(chunk)
    return b"".join(chunks), content_type


def tool_command(executable: str, arguments: list[str]) -> list[str]:
    if Path(executable).suffix.casefold() in {".bat", ".cmd"}:
        return [os.environ.get("COMSPEC", "cmd.exe"), "/d", "/c", executable, *arguments]
    return [executable, *arguments]


def render_pdf(pdf_path: Path, output_dir: Path, dpi: int) -> list[Path]:
    old_pages = list(output_dir.glob("page_*.png"))
    rendered: list[Path] = []
    try:
        import pymupdf  # type: ignore
    except ImportError:
        pymupdf = None
    if pymupdf is not None:
        document = pymupdf.open(pdf_path)
        scale = dpi / 72.0
        matrix = pymupdf.Matrix(scale, scale)
        for index, page in enumerate(document, 1):
            target = output_dir / f"page_{index:03d}.png"
            page.get_pixmap(matrix=matrix, alpha=False).save(target)
            rendered.append(target)
        document.close()
    elif pdftoppm := shutil.which("pdftoppm"):
        prefix = output_dir / "rendered-page"
        command = tool_command(
            pdftoppm,
            ["-png", "-r", str(dpi), str(pdf_path), str(prefix)],
        )
        result = subprocess.run(command, capture_output=True, text=True, timeout=300, check=False)
        if result.returncode != 0:
            raise RuntimeError(f"pdftoppm failed: {result.stderr.strip()}")
        raw_pages = sorted(output_dir.glob("rendered-page-*.png"))
        for index, raw_page in enumerate(raw_pages, 1):
            target = output_dir / f"page_{index:03d}.png"
            raw_page.replace(target)
            rendered.append(target)
    else:
        raise RuntimeError("PDF rendering requires PyMuPDF or a working pdftoppm")
    if not rendered:
        raise RuntimeError(f"PDF renderer produced no pages: {pdf_path}")
    rendered_set = {path.resolve() for path in rendered}
    for old_page in old_pages:
        if old_page.resolve() not in rendered_set:
            old_page.unlink()
    return rendered


def fetch_product(
    product: dict[str, Any],
    *,
    assets_root: Path,
    session: requests.Session,
    timeout: int,
    max_bytes: int,
    dpi: int,
) -> tuple[dict[str, Any], bool]:
    product_dir = assets_root / product["product_id"]
    product_dir.mkdir(parents=True, exist_ok=True)
    metadata_path = product_dir / "asset_manifest.json"
    previous = load_json(metadata_path) if metadata_path.exists() else None
    assets: list[dict[str, Any]] = []
    content_changed = False

    for schematic in product["schematics"]:
        url = schematic["url"]
        print(f"[FETCH] {product['product_name']}: {safe_log_url(url)}")
        data, content_type = download_bytes(session, url, timeout, max_bytes)
        declared_extension = choose_extension(url, content_type)
        extension = detect_extension(data)
        if extension != declared_extension:
            print(
                f"[WARN] declared {declared_extension} but content is {extension}; using detected type"
            )
        ordinal = schematic["ordinal"] + 1
        source_file = product_dir / f"source_{ordinal:03d}{extension}"
        digest = sha256_bytes(data)
        if write_bytes_if_changed(source_file, data):
            content_changed = True

        if extension == ".pdf":
            page_dir = product_dir / f"source_{ordinal:03d}_pages"
            page_dir.mkdir(parents=True, exist_ok=True)
            page_paths = render_pdf(source_file, page_dir, dpi)
        else:
            page_paths = [source_file]
        pages = [
            {
                "page": index,
                "path": page.relative_to(PROJECT_ROOT).as_posix(),
                "sha256": sha256_file(page),
            }
            for index, page in enumerate(page_paths, 1)
        ]
        assets.append(
            {
                "ordinal": schematic["ordinal"],
                "kind": schematic["kind"],
                "source_url": url,
                "source_path": source_file.relative_to(PROJECT_ROOT).as_posix(),
                "sha256": digest,
                "bytes": len(data),
                "content_type": content_type.split(";", 1)[0].strip().lower(),
                "pages": pages,
            }
        )

    fingerprint = sha256_bytes(canonical_json_bytes(assets))
    if previous and previous.get("assets_sha256") == fingerprint:
        fetched_at = previous["fetched_at"]
    else:
        fetched_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
        content_changed = True
    metadata = {
        "schema_version": 1,
        "product_id": product["product_id"],
        "product_name": product["product_name"],
        "product_input_sha256": product["input_sha256"],
        "assets_sha256": fingerprint,
        "fetched_at": fetched_at,
        "assets": assets,
    }
    metadata_changed = write_json_if_changed(metadata_path, metadata)
    return metadata, content_changed or metadata_changed


def select_products(manifest: dict[str, Any], args: argparse.Namespace) -> list[dict[str, Any]]:
    if args.all:
        if not args.confirm_all:
            raise ValueError("--all requires --confirm-all")
        return list(manifest["products"])
    selected: list[dict[str, Any]] = []
    for product_id in args.product_id:
        selected.append(find_product(manifest, product_id=product_id))
    for product_name in args.product_name:
        selected.append(find_product(manifest, product_name=product_name))
    if not selected:
        raise ValueError("Select at least one --product-id/--product-name, or use --all --confirm-all")
    unique = {item["product_id"]: item for item in selected}
    return [unique[key] for key in sorted(unique)]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch and fingerprint schematic assets")
    parser.add_argument("--manifest", type=Path, default=PROJECT_ROOT / "state" / "product_manifest.json")
    parser.add_argument("--assets-root", type=Path, default=PROJECT_ROOT / "artifacts" / "schematics")
    parser.add_argument("--product-id", action="append", default=[])
    parser.add_argument("--product-name", action="append", default=[])
    parser.add_argument("--all", action="store_true")
    parser.add_argument("--confirm-all", action="store_true")
    parser.add_argument("--timeout", type=int, default=60)
    parser.add_argument("--max-bytes", type=int, default=50 * 1024 * 1024)
    parser.add_argument("--pdf-dpi", type=int, default=180)
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest = load_manifest(args.manifest)
    selected = select_products(manifest, args)
    print(json.dumps([{"product_id": p["product_id"], "product_name": p["product_name"]} for p in selected], ensure_ascii=False, indent=2))
    if args.dry_run:
        return 0
    session = requests.Session()
    session.headers.update({"User-Agent": "M5Stack-Schematic-Pipeline/1.0"})
    failures: list[dict[str, str]] = []
    for product in selected:
        try:
            _, changed = fetch_product(
                product,
                assets_root=args.assets_root,
                session=session,
                timeout=args.timeout,
                max_bytes=args.max_bytes,
                dpi=args.pdf_dpi,
            )
            print(f"[{'UPDATED' if changed else 'UNCHANGED'}] {product['product_name']}")
        except Exception as exc:
            failures.append({"product_id": product["product_id"], "error": str(exc)})
            print(f"[FAIL] {product['product_name']}: {exc}", file=sys.stderr)
    if failures:
        print(json.dumps({"failures": failures}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
