from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
import unicodedata
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def stable_product_id(product_name: str, source_path: str) -> str:
    normalized = unicodedata.normalize("NFKD", product_name)
    ascii_name = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_name.lower()).strip("-")
    slug = slug[:48] or "product"
    suffix = sha256_bytes(source_path.casefold().encode("utf-8"))[:12]
    return f"{slug}-{suffix}"


def sanitize_output_stem(product_name: str) -> str:
    stem = re.sub(r'[<>:"/\\|?*]', "_", product_name).strip().rstrip(".")
    stem = re.sub(r"\s+", " ", stem)
    return (stem[:180] or "Unknown").rstrip(". ")


def canonical_json_bytes(data: Any) -> bytes:
    text = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    return text.encode("utf-8")


def write_bytes_if_changed(path: Path, content: bytes) -> bool:
    if path.exists() and path.read_bytes() == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()
    return True


def write_json_if_changed(path: Path, data: Any) -> bool:
    return write_bytes_if_changed(path, canonical_json_bytes(data))


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_manifest(path: Path) -> dict[str, Any]:
    manifest = load_json(path)
    if manifest.get("schema_version") != 1 or not isinstance(manifest.get("products"), list):
        raise ValueError(f"Unsupported product manifest: {path}")
    return manifest


def find_product(
    manifest: dict[str, Any], *, product_id: str | None = None, product_name: str | None = None
) -> dict[str, Any]:
    if bool(product_id) == bool(product_name):
        raise ValueError("Specify exactly one of product_id or product_name")
    field = "product_id" if product_id else "product_name"
    value = product_id or product_name
    matches = [item for item in manifest["products"] if item.get(field) == value]
    if not matches:
        raise KeyError(f"Product not found by {field}: {value}")
    if len(matches) > 1:
        ids = ", ".join(item["product_id"] for item in matches)
        raise ValueError(f"Ambiguous product name {value!r}; use product_id: {ids}")
    return matches[0]
