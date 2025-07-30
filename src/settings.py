import json
import os
import sys

hardcoded_settings = {
    "windows": {"main": {"width": 800, "height": 600, "x": 0, "y": 0}}
}

hardcoded_theme = {
    "colors": {
        "accent": "#40706b",
        "background": "#0c1414",
        "light-background": "#142422",
        "text": "#bdd9d6",
        "button": "#6aada7",
        "selection-background": "#6aada7",
        "selection-text": "#142422",
        "scrollbar-background": "#40706b",
        "scrollbar-trough": "#0c1414",
        "scrollbar-border": "#0c1414",
        "scrollbar-arrow": "#6aada7",
        "scrollbar-hover": "#5bbdb7",
        "scrollbar-active-background": "#40706b",
        "scrollbar-active-arrow": "#bdd9d6",
        "scrollbar-disabled-background": "#22302e",
        "scrollbar-disabled-arrow": "#40706b",
        "scrollbar-highlight": "#40706b",
        "scrollbar-shadow": "#0c1414",
    },
    "fonts": {
        "ui-text": "Segoe UI",
        "ui-heading": "Segoe UI Semibold",
        "ui-text-size": 13,
        "ui-heading-size": 18,
        "editor-text": "Courier New",
        "editor-text-size": 15,
    },
    "editor": {
        "keyword": "#a68dcd",
        "string": "#ace88d",
        "comment": "#808080",
        "function": "#1760bc",
        "operator": "#cc8850",
        "number": "#ffbf0d",
    },
}


def _get_data_path(filename):
    if getattr(sys, "frozen", False):
        base_path = os.path.dirname(sys.executable)
        data_path = os.path.join(base_path, "data", filename)
        if os.path.exists(data_path):
            return data_path
    base_path = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_path, "data", filename)
    return data_path


def load():
    """
    Loads settings from the settings.json file located in the data directory.
    Returns:
        dict: The settings as a dictionary.
    """
    settings_path = _get_data_path("settings.json")
    if not os.path.exists(settings_path):
        print("[ERR] Settings file not found, using hardcoded defaults.", flush=True)
        return hardcoded_settings
    with open(settings_path, "r", encoding="utf-8") as f:
        try:
            print("[INF] Settings file loaded successfully.", flush=True)
            return json.load(f)
        except ValueError:
            return hardcoded_settings


def theme():
    """
    Returns the theme settings.
    Returns:
        dict: The theme settings.
    """
    theme_path = _get_data_path("theme.json")
    if not os.path.exists(theme_path):
        print("[ERR] Theme file not found", flush=True)
        return hardcoded_theme
    with open(theme_path, "r", encoding="utf-8") as f:
        try:
            print("[INF] Theme file loaded successfully.", flush=True)
            return json.load(f)
        except ValueError:
            return hardcoded_theme
