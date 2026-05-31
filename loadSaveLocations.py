import json

def load(locType: str):
    """":param locType - Either 'Phone' or 'Car'"""
    PATH = f"storage/last{locType}Locations.json"
    with open(PATH, "r") as f:
        return json.load(f)

def save(locType: str, data: dict):
    """":param locType - Either 'Phone' or 'Car'"""
    PATH = f"storage/last{locType}Locations.json"
    with open(PATH, "w") as f:
        json.dump(data, f, indent=4)