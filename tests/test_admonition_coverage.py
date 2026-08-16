import unittest

import pytest

ADMONITION_TYPES = [
    "note",
    "abstract",
    "summary",
    "tldr",
    "info",
    "tip",
    "hint",
    "important",
    "success",
    "check",
    "done",
    "question",
    "help",
    "faq",
    "warning",
    "caution",
    "attention",
    "failure",
    "fail",
    "missing",
    "danger",
    "error",
    "bug",
    "example",
    "quote",
    "cite",
]


class TestAdmonitionCoverage(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _inject_css(self, css_source, css_min):
        self.css_source = css_source
        self.css_min = css_min

    def test_source_css_covers_all_types(self):
        """Source CSS must define rules for every MkDocs admonition type."""
        content = self.css_source.read_text()
        missing = [
            t for t in ADMONITION_TYPES if f".admonition.{t}" not in content
        ]

        self.assertFalse(
            missing, f"Missing admonition rules in source CSS: {missing}"
        )

    def test_min_css_covers_all_types(self):
        """Minified CSS must define rules for every MkDocs admonition type."""
        content = self.css_min.read_text()
        missing = [
            t for t in ADMONITION_TYPES if f".admonition.{t}" not in content
        ]

        self.assertFalse(
            missing, f"Missing admonition rules in minified CSS: {missing}"
        )

    def test_source_and_min_in_sync(self):
        """Source and minified CSS must cover the exact same set of admonition types."""
        source = self.css_source.read_text()
        minified = self.css_min.read_text()

        for admonition_type in ADMONITION_TYPES:
            in_src = f".admonition.{admonition_type}" in source
            in_min = f".admonition.{admonition_type}" in minified
            with self.subTest(admonition_type=admonition_type):
                self.assertEqual(in_src, in_min)
