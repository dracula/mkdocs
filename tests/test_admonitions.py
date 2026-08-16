"""Tests for PR #33 — admonition styles with Dracula colors and Font Awesome icons."""

import re
from pathlib import Path

CSS_SOURCE = (
    Path(__file__).parent.parent / "template" / "assets" / "css" / "mkdocs.css"
)
CSS_MIN = (
    Path(__file__).parent.parent
    / "mkdocs_dracula_theme"
    / "assets"
    / "css"
    / "mkdocs.min.css"
)

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


class TestAdmonitionCoverage:
    def test_source_css_covers_all_types(self):
        """Source CSS must define rules for every MkDocs admonition type."""
        content = CSS_SOURCE.read_text()
        missing = [
            t for t in ADMONITION_TYPES if f".admonition.{t}" not in content
        ]
        assert not missing, (
            f"Missing admonition rules in source CSS: {missing}"
        )

    def test_min_css_covers_all_types(self):
        """Minified CSS must define rules for every MkDocs admonition type."""
        content = CSS_MIN.read_text()
        missing = [
            t for t in ADMONITION_TYPES if f".admonition.{t}" not in content
        ]
        assert not missing, (
            f"Missing admonition rules in minified CSS: {missing}"
        )

    def test_source_and_min_in_sync(self):
        """Source and minified CSS must cover the exact same set of admonition types."""
        source = CSS_SOURCE.read_text()
        minified = CSS_MIN.read_text()
        for t in ADMONITION_TYPES:
            in_src = f".admonition.{t}" in source
            in_min = f".admonition.{t}" in minified
            assert in_src == in_min, (
                f".admonition.{t}: source={in_src}, minified={in_min} — files are out of sync"
            )


class TestAdmonitionIcons:
    def test_tip_uses_lightbulb_not_fire_in_source(self):
        """tip/hint/important must use fa-lightbulb-o (\\f0eb), not fa-fire (\\f06d)."""
        content = CSS_SOURCE.read_text()
        assert r"\f0eb" in content, (
            r"Source CSS missing lightbulb icon (\f0eb) for tip/hint/important"
        )
        assert r"\f06d" not in content, (
            r"Source CSS must not use fire icon (\f06d)"
        )

    def test_tip_uses_lightbulb_not_fire_in_min(self):
        """Minified CSS: tip/hint/important must use fa-lightbulb-o (\\f0eb)."""
        content = CSS_MIN.read_text()
        assert r"\f0eb" in content, (
            r"Minified CSS missing lightbulb icon (\f0eb)"
        )
        assert r"\f06d" not in content, (
            r"Minified CSS must not use fire icon (\f06d)"
        )

    def test_all_icon_codepoints_present_in_source(self):
        """Each admonition type must reference its expected Font Awesome codepoint."""
        content = CSS_SOURCE.read_text()
        seen_codepoints = set()
        for admonition_type, codepoint in EXPECTED_ICONS.items():
            if codepoint not in seen_codepoints:
                assert codepoint in content, (
                    f"Icon codepoint {codepoint} for .admonition.{admonition_type} "
                    f"not found in source CSS"
                )
                seen_codepoints.add(codepoint)


class TestAdmonitionColors:
    def test_source_css_uses_dracula_variables(self):
        """Admonition styles must use CSS variables, not hardcoded hex values."""
        content = CSS_SOURCE.read_text()
        # Extract only the admonition section
        start = content.find(".admonition {")
        assert start != -1, "Admonition base rule not found"
        admonition_section = content[start:]
        # Must not contain hex colors in the admonition section
        assert not re.search(r":\s*#[0-9a-fA-F]{3,6}", admonition_section), (
            "Admonition styles must use CSS variables (var(--color)), not hardcoded hex values"
        )

    def test_expected_color_variables_present(self):
        """Each admonition type must reference its expected Dracula color variable."""
        content = CSS_SOURCE.read_text()
        for admonition_type, color_var in EXPECTED_COLORS.items():
            pattern = rf"\.admonition\.{admonition_type}[^{{]*\{{[^}}]*{re.escape(color_var)}"
            assert re.search(pattern, content), (
                f".admonition.{admonition_type} should reference {color_var}"
            )


class TestMinifiedCSSFormat:
    def test_admonition_section_has_no_comments(self):
        """The admonition block in mkdocs.min.css must not contain CSS comments."""
        content = CSS_MIN.read_text()
        admonition_start = content.find(".admonition{")
        assert admonition_start != -1, (
            "Admonition CSS not found in minified file"
        )
        admonition_section = content[admonition_start:]
        assert "/*" not in admonition_section, (
            "Minified CSS must not contain comments — strip them before appending to .min.css"
        )

    def test_admonition_section_has_no_indentation(self):
        """The admonition block in mkdocs.min.css must not contain indented lines."""
        content = CSS_MIN.read_text()
        admonition_start = content.find(".admonition{")
        assert admonition_start != -1
        admonition_section = content[admonition_start:]
        assert "\n    " not in admonition_section, (
            "Minified CSS must not contain indented lines"
        )

    def test_admonition_uses_shorthand_values(self):
        """Minified CSS should use shorthand values (e.g. .5rem not 0.5rem)."""
        content = CSS_MIN.read_text()
        admonition_start = content.find(".admonition{")
        assert admonition_start != -1
        admonition_section = content[admonition_start:]
        assert "0.5rem" not in admonition_section, (
            "Minified CSS should use .5rem instead of 0.5rem"
        )
        assert "0.75rem" not in admonition_section, (
            "Minified CSS should use .75rem instead of 0.75rem"
        )
