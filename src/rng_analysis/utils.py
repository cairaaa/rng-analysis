import pandas as pd

from rng_analysis.load import load_data


def summarize_trials() -> pd.DataFrame:
    df = load_data()
    summary = (
        df.groupby("trial")
            .agg(
                games=("game_number", "nunique"),
                observations=("minigame", "count"),
                first_game=("timestamp", "min"),
                last_game=("timestamp", "max"),
            )
            .reset_index()
    )
    return summary
