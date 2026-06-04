import json

def load(basename: str):
    PATH = f"storage/{basename}.json"
    with open(PATH, "r") as f:
        return json.load(f)

def save(basename: str, data: dict):
    PATH = f"storage/{basename}.json"
    with open(PATH, "w") as f:
        json.dump(data, f, indent=4)