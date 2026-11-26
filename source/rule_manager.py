"""Load ACL rules from a JSON configuration file."""
import json
from pathlib import Path


def load_rules(config_path):
    path = Path(config_path)
    with path.open("r", encoding="utf-8") as file:
        config = json.load(file)
    return config.get("rules", []), config.get("default_action", "DENY")
