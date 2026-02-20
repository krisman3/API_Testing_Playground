import json
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR/ "config" / "environments"


def load_config(env: str):
    config_path = CONFIG_DIR / f"{env}.json"
    if not config_path.exists():
        raise FileNotFoundError(f"{config_path} not found.")

    with config_path.open('r') as file:
        return json.load(file)