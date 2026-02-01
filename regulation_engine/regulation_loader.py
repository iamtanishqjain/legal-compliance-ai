import json

def load_obligations(path):
    with open(path, "r") as f:
        return json.load(f)
