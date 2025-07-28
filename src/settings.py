import json
import os
import sys

hardcoded_settings = {
    "windows": {"main": {"width": 800, "height": 600, "x": 0, "y": 0}}
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
        return {}  # TODO: Write a proper default theme
    with open(theme_path, "r", encoding="utf-8") as f:
        try:
            print("[INF] Theme file loaded successfully.", flush=True)
            return json.load(f)
        except ValueError:
            return {}
