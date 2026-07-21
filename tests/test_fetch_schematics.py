from __future__ import annotations

import unittest

from scripts.fetch_schematics import (
    choose_extension,
    detect_extension,
    safe_log_url,
    tool_command,
    validate_magic,
)


class FetchSchematicTests(unittest.TestCase):
    def test_extension_uses_url_path_before_query(self) -> None:
        self.assertEqual(choose_extension("https://e.test/a.webp?rev=2", "application/octet-stream"), ".webp")

    def test_extension_falls_back_to_content_type(self) -> None:
        self.assertEqual(choose_extension("https://e.test/download", "application/pdf; charset=binary"), ".pdf")

    def test_safe_log_url_removes_query_and_fragment(self) -> None:
        self.assertEqual(safe_log_url("https://e.test/a.png?token=secret#x"), "https://e.test/a.png")

    def test_webp_magic_is_strict(self) -> None:
        validate_magic(b"RIFF\x00\x00\x00\x00WEBPdata", ".webp")
        with self.assertRaises(ValueError):
            validate_magic(b"RIFF\x00\x00\x00\x00WAVEdata", ".webp")

    def test_detects_mislabeled_png(self) -> None:
        data = b"\x89PNG\r\n\x1a\nrest"
        self.assertEqual(detect_extension(data), ".png")
        with self.assertRaises(ValueError):
            validate_magic(data, ".webp")

    def test_cmd_wrapper_uses_command_interpreter(self) -> None:
        command = tool_command(r"C:\tools\pdftoppm.cmd", ["-png", "input.pdf"])
        self.assertEqual(command[1:3], ["/d", "/c"])
        self.assertEqual(command[3], r"C:\tools\pdftoppm.cmd")


if __name__ == "__main__":
    unittest.main()
