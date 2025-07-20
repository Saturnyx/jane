import json
import os


def load_settings():
    """
    Loads settings from the settings.json file located in the data directory.
    Returns:
        dict: The settings as a dictionary.
    """
    settings_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "data", "settings.json"
    )
    if not os.path.exists(settings_path):
        return {}
    with open(settings_path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except ValueError:
            return {}
