import unittest
from gencontent import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title_basic_h1(self):
        markdown = "# Hello"
        result = extract_title(markdown)
        self.assertEqual(result, "Hello")

    def test_extract_title_strips_whitespace(self):
        markdown = "#   Tolkien Fan Club   "
        result = extract_title(markdown)
        self.assertEqual(result, "Tolkien Fan Club")

    def test_extract_title_h1_inside_multiline(self):
        markdown = "This is some text\n# My Page\nMore text"
        result = extract_title(markdown)
        self.assertEqual(result, "My Page")

    def test_extract_title_ignores_h2(self):
        markdown = "## Not the title"
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_extract_title_no_h1(self):
        markdown = "Some paragraph\nAnother line"
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_extract_title_mixed_headers(self):
        markdown = "## Subtitle\n# Real Title\n### Smaller header"
        result = extract_title(markdown)
        self.assertEqual(result, "Real Title")
