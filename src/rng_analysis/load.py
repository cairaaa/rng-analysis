from pathlib import Path

import pandas as pd

DATA_DIR = Path("data")

def load_data() -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / "games.csv")
