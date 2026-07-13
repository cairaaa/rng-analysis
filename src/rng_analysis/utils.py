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

def calc_games(df: pd.DataFrame) -> int:
    return df[["trial", "game_number"]].drop_duplicates().shape[0]

def calc_observations(df: pd.DataFrame) -> int:
    return len(df)

def calc_minigame_counts(df: pd.DataFrame) -> pd.Series:
    return df["minigame"].value_counts()

def calc_mean_frequency(df: pd.DataFrame) -> float:
    counts = calc_minigame_counts(df)
    return float(round(counts.mean(), 2))

def calc_std_frequency(df: pd.DataFrame) -> float:
    counts = calc_minigame_counts(df)
    return float(round(counts.std(ddof=1), 2))

def calc_frequency_range(df: pd.DataFrame) -> tuple[int, int]:
    counts = calc_minigame_counts(df)
    return int(counts.min()), int(counts.max())
