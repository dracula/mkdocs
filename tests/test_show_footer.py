"""Tests for PR #32 — show_footer config option."""

from pathlib import Path

import yaml

THEME_YML = (
    Path(__file__).parent.parent / "mkdocs_dracula_theme" / "mkdocs_theme.yml"
)
FOOTER_TEXT = "Made with Dracula Theme for MkDocs"


class TestShowFooterDefault:
    def test_default_config_declares_show_footer(self):
        """mkdocs_theme.yml must declare show_footer key."""
        config = yaml.safe_load(THEME_YML.read_text())
        assert "show_footer" in config, (
            "show_footer key missing from mkdocs_theme.yml"
        )

    def test_default_value_is_true(self):
        """Default value of show_footer must be True (backwards-compatible)."""
        config = yaml.safe_load(THEME_YML.read_text())
        assert config["show_footer"] is True

    def test_footer_rendered_by_default(self, build_site):
        """Footer is visible when show_footer is not set."""
        html = build_site()
        assert FOOTER_TEXT in html

    def test_footer_rendered_when_explicitly_true(self, build_site):
        """Footer is visible when show_footer: true."""
        html = build_site("show_footer: true")
        assert FOOTER_TEXT in html

    def test_footer_hidden_when_false(self, build_site):
        """Footer is absent when show_footer: false."""
        html = build_site("show_footer: false")
        assert FOOTER_TEXT not in html

    def test_base_template_has_conditional(self):
        """base.html must wrap the footer include with show_footer conditional."""
        base = (
            Path(__file__).parent.parent / "mkdocs_dracula_theme" / "base.html"
        ).read_text()
        assert "config.theme.show_footer" in base, (
            "base.html must guard the footer include with {% if config.theme.show_footer %}"
        )
