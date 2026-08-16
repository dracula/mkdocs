import re
import unittest

import pytest

EXPECTED_COLORS = {
    "note": "--purple",
    "example": "--purple",
    "abstract": "--cyan",
    "summary": "--cyan",
    "tldr": "--cyan",
    "info": "--cyan",
    "tip": "--green",
    "hint": "--green",
    "important": "--green",
    "success": "--green",
    "check": "--green",
    "done": "--green",
    "question": "--yellow",
    "help": "--yellow",
    "faq": "--yellow",
    "warning": "--orange",
    "caution": "--orange",
    "attention": "--orange",
    "failure": "--pink",
    "fail": "--pink",
    "missing": "--pink",
    "danger": "--red",
    "error": "--red",
    "bug": "--red",
    "quote": "--grey",
    "cite": "--grey",
}


class TestAdmonitionColors(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _inject_css(self, css_source):
        self.css_source = css_source

    def test_source_css_uses_dracula_variables(self):
        """Admonition styles must use CSS variables, not hardcoded hex values."""
        content = self.css_source.read_text()
        start = content.find(".admonition {")

        self.assertNotEqual(start, -1, "Admonition base rule not found")

        admonition_section = content[start:]

        self.assertIsNone(
            re.search(r":\s*#[0-9a-fA-F]{3,6}", admonition_section),
            "Admonition styles must use CSS variables (var(--color)), not hardcoded hex values",
        )

    def test_expected_color_variables_present(self):
        """Each admonition type must reference its expected Dracula color variable."""
        content = self.css_source.read_text()

        for admonition_type, color_var in EXPECTED_COLORS.items():
            pattern = rf"\.admonition\.{admonition_type}[^{{]*\{{[^}}]*{re.escape(color_var)}"
            with self.subTest(admonition_type=admonition_type):
                self.assertIsNotNone(re.search(pattern, content))
