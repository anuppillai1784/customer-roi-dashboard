import json
from pathlib import Path

DEFAULT_CONFIG_PATH = Path(__file__).with_name("config.json")


def load_config(path=DEFAULT_CONFIG_PATH):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)
