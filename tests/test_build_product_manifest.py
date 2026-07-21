from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.build_product_manifest import build_manifest, clean_content, extract_schematic_urls


class ProductManifestTests(unittest.TestCase):
    def test_extracts_image_with_query_string(self) -> None:
        content = '# Demo\n\n## 原理图\n<img src="https://example.test/a.webp?v=2">\n'
        self.assertEqual(
            extract_schematic_urls(content),
            [{"ordinal": 0, "kind": "image", "url": "https://example.test/a.webp?v=2"}],
        )

    def test_falls_back_to_pdf(self) -> None:
        content = "# Demo\n\n## 原理图\n[PDF](https://example.test/a.pdf?rev=2)\n"
        self.assertEqual(extract_schematic_urls(content)[0]["kind"], "pdf")

    def test_clean_content_removes_component_tags(self) -> None:
        content = "before<TabPanel name=\"x\">secret</TabPanel>after"
        self.assertEqual(clean_content(content), "beforeafter")

    def test_manifest_is_deterministic_and_excludes_published_tree(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "zh_CN"
            (root / "unit").mkdir(parents=True)
            (root / "schematic").mkdir(parents=True)
            body = '# Same Name\n\n<span>SKU:U001</span>\n\n## 原理图\n<img src="https://e.test/a.png">\n'
            (root / "unit" / "a.md").write_text(body, encoding="utf-8")
            (root / "unit" / "b.md").write_text(body.replace("a.png", "b.png"), encoding="utf-8")
            (root / "schematic" / "ignore.md").write_text(body, encoding="utf-8")

            first = build_manifest(root)
            second = build_manifest(root)

            self.assertEqual(first, second)
            self.assertEqual(first["summary"]["products"], 2)
            self.assertEqual(first["summary"]["duplicate_product_names"], ["Same Name"])
            filenames = {item["output_filename"] for item in first["products"]}
            self.assertEqual(len(filenames), 2)
            self.assertTrue(all(item["sku"] == "U001" for item in first["products"]))

    def test_missing_title_uses_source_filename_and_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "zh_CN"
            (root / "unit").mkdir(parents=True)
            body = '## 原理图\n<img src="https://e.test/a.png">\n'
            (root / "unit" / "fallback-name.md").write_text(body, encoding="utf-8")

            manifest = build_manifest(root)

            product = manifest["products"][0]
            self.assertEqual(product["product_name"], "fallback-name")
            self.assertTrue(product["title_missing"])
            self.assertEqual(
                manifest["summary"]["missing_product_titles"], ["unit/fallback-name.md"]
            )


if __name__ == "__main__":
    unittest.main()
