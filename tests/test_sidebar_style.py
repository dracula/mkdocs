import unittest

import pytest


class TestSidebarChevronColor(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _inject_css(self, css_source, css_min):
        self.css_source = css_source
        self.css_min = css_min

    def test_source_chevron_uses_palette_variables(self):
        """The chevron must be themed with var(--purple)/var(--cyan)/var(--pink)."""
        content = self.css_source.read_text()

        self.assertIn("var(--purple)", content)
        self.assertIn("var(--cyan)", content)
        self.assertIn("var(--pink)", content)

    def test_source_chevron_has_no_hardcoded_stroke_color(self):
        """The old hardcoded black/white SVG strokes must be gone."""
        content = self.css_source.read_text()

        self.assertNotIn("rgba%280,0,0,.5%29", content)
        self.assertNotIn("rgba%28248,248,242,1%29", content)

    def test_min_chevron_uses_palette_variables(self):
        content = self.css_min.read_text()

        self.assertIn("var(--purple)", content)
        self.assertIn("var(--cyan)", content)
        self.assertIn("var(--pink)", content)

    def test_min_chevron_has_no_hardcoded_stroke_color(self):
        content = self.css_min.read_text()

        self.assertNotIn("rgba%280,0,0,.5%29", content)
        self.assertNotIn("rgba%28248,248,242,1%29", content)


class TestSubmenuIndentation(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _inject_css(self, css_source, css_min):
        self.css_source = css_source
        self.css_min = css_min

    def test_source_submenu_has_no_percentage_indent(self):
        """Percentage-based indentation must be replaced by a fixed rem indent."""
        content = self.css_source.read_text()
        start = content.find(".drac-box-ternary {")

        self.assertNotEqual(start, -1, ".drac-box-ternary rule not found")

        rule = content[start : content.find("}", start)]

        self.assertNotIn("10%", rule)
        self.assertIn("0.75rem", rule)

    def test_source_submenu_has_left_border_guide(self):
        content = self.css_source.read_text()
        start = content.find(".drac-box-ternary {")
        rule = content[start : content.find("}", start)]

        self.assertIn("border-left", rule)
        self.assertIn("var(--greySecondary)", rule)

    def test_min_submenu_has_no_percentage_indent(self):
        content = self.css_min.read_text()
        start = content.find(".drac-box-ternary{")

        self.assertNotEqual(
            start, -1, ".drac-box-ternary rule not found in minified CSS"
        )

        rule = content[start : content.find("}", start)]

        self.assertNotIn("10%", rule)
        self.assertIn(".75rem", rule)
