from pathlib import Path
import yaml
import pickle

def load_config(path: Path):
    with open(path, "r") as f:
        config = yaml.safe_load(f)
    return config

def load_index(path):
    with open(path, "rb") as f:
        return pickle.load(f)