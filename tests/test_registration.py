import importlib.metadata
import unittest


def _entry_points_for(group):
    entry_points = importlib.metadata.entry_points()
    if hasattr(entry_points, "select"):
        return entry_points.select(group=group)
    return entry_points.get(group, [])


class TestThemeRegistration(unittest.TestCase):
    def test_dracula_theme_is_registered_as_mkdocs_theme(self):
        names = [ep.name for ep in _entry_points_for("mkdocs.themes")]

        self.assertIn("dracula", names)

    def test_dracula_entry_point_resolves_to_theme_package(self):
        entry_points = [
            ep
            for ep in _entry_points_for("mkdocs.themes")
            if ep.name == "dracula"
        ]
        (entry_point,) = entry_points

        self.assertEqual(entry_point.value, "mkdocs_dracula_theme")
