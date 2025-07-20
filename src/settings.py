import json
import os

hardcoded = {"windows": {"main": {"width": 800, "height": 600, "x": 0, "y": 0}}}


def load():
    """
    Loads settings from the settings.json file located in the data directory.
    Returns:
        dict: The settings as a dictionary.
    """
    settings_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "data", "settings.json"
    )
    if not os.path.exists(settings_path):
        print("[ERR] Settings file not found, using hardcoded defaults.", flush=True)
        return hardcoded
    with open(settings_path, "r", encoding="utf-8") as f:
        try:
            print("[INF] Settings file loaded successfully.", flush=True)
            return json.load(f)
        except ValueError:
            return hardcoded
