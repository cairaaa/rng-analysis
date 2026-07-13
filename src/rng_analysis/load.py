import json
from pathlib import Path

import pandas as pd

DATA_DIR = Path("data")

def load_data(trial: int | None = None) -> pd.DataFrame:
    df = pd.read_csv(DATA_DIR / "games.csv")
    if trial is not None:
        df = df[df["trial"] == trial]
    return df

def load_results(trial: int | None = None) -> dict:
    path = DATA_DIR / "results.json"
    with path.open("r") as file:
        data = json.load(file)
    return data

