import unittest

import pytest

EXPECTED_ICONS = {
    "note": r"\f040",
    "abstract": r"\f0ea",
    "summary": r"\f0ea",
    "tldr": r"\f0ea",
    "info": r"\f05a",
    "tip": r"\f0eb",
    "hint": r"\f0eb",
    "important": r"\f0eb",
    "success": r"\f058",
    "check": r"\f058",
    "done": r"\f058",
    "question": r"\f059",
    "help": r"\f059",
    "faq": r"\f059",
    "warning": r"\f071",
    "caution": r"\f071",
    "attention": r"\f071",
    "failure": r"\f057",
    "fail": r"\f057",
    "missing": r"\f057",
    "danger": r"\f0e7",
    "error": r"\f0e7",
    "bug": r"\f188",
    "example": r"\f03a",
    "quote": r"\f10d",
    "cite": r"\f10d",
}


class TestAdmonitionIcons(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _inject_css(self, css_source, css_min):
        self.css_source = css_source
        self.css_min = css_min

    def test_tip_uses_lightbulb_not_fire_in_source(self):
        """tip/hint/important must use fa-lightbulb-o (\\f0eb), not fa-fire (\\f06d)."""
        content = self.css_source.read_text()

        self.assertIn(r"\f0eb", content)
        self.assertNotIn(r"\f06d", content)

    def test_tip_uses_lightbulb_not_fire_in_min(self):
        """Minified CSS: tip/hint/important must use fa-lightbulb-o (\\f0eb)."""
        content = self.css_min.read_text()

        self.assertIn(r"\f0eb", content)
        self.assertNotIn(r"\f06d", content)

    def test_all_icon_codepoints_present_in_source(self):
        """Each admonition type must reference its expected Font Awesome codepoint."""
        content = self.css_source.read_text()
        seen_codepoints = set(EXPECTED_ICONS.values())

        for codepoint in seen_codepoints:
            with self.subTest(codepoint=codepoint):
                self.assertIn(codepoint, content)
