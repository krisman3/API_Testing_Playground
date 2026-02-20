import json
from pathlib import Path

def get_env_from_json(filename, param:str):
    path = Path(filename)

    if not path.exists():
        raise FileNotFoundError(f"{filename} not found")

    with open(filename, 'r') as file:
        content = json.load(file)

    if param not in content:
        raise KeyError(f"{param} not found in config")

    return content[param]