import json
import os

hardcoded = {"windows": {"main": {"width": 800, "height": 600, "x": 0, "y": 0}}}


def load():
    """
    Loads settings from the settings.json file located in the data directory.
    Returns:
        dict: The settings as a dictionary.
    """
    theme_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "data", "settings.json"
    )
    if not os.path.exists(theme_path):
        print("[ERR] Settings file not found, using hardcoded defaults.", flush=True)
        return hardcoded
    with open(theme_path, "r", encoding="utf-8") as f:
        try:
            print("[INF] Settings file loaded successfully.", flush=True)
            return json.load(f)
        except ValueError:
            return hardcoded

def theme():
    """
    Returns the theme settings.
    Returns:
        dict: The theme settings.
    """
    theme_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "data", "theme.json"
    )
    if not os.path.exists(theme_path):
        print("[ERR] Theme file not found", flush=True)
        return {}  # TODO: Write a proper default theme
    with open(theme_path, "r", encoding="utf-8") as f:
        try:
            print("[INF] Theme file loaded successfully.", flush=True)
            return json.load(f)
        except ValueError:
            return {}
