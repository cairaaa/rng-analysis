import numpy as np
from scipy import stats

from rng_analysis.load import load_data
from rng_analysis.utils import summarize_trials


def calculate_chi_square(trial: int | None = None) -> tuple[float, float]:
    df = load_data(trial)
    observed = df["minigame"].value_counts()
    chi_sq, p = stats.chisquare(observed)
    return chi_sq, p

def simulate_trial(games: int, rng: np.random.Generator) -> float:
    ranks = np.argsort(rng.random((games, 26)), axis=1)[:, :8]
    counts = np.bincount(ranks.ravel(), minlength=26)
    expected = counts.sum() / 26
    chi_sq = np.sum((counts - expected) ** 2 / expected)
    return chi_sq

def simulate_null_distribution(
    trial: int | None = None, 
    simulations: int = 100000,
    seed: int = 42
) -> np.ndarray:
    df = summarize_trials()
    if trial is None:
        games = int(df["games"].sum())
    else:
        games = int(df.loc[df["trial"] == trial, "games"].iloc[0])
    rng = np.random.default_rng(seed)
    chi_sq_values = np.empty(simulations)
    for i in range(simulations):
        chi_sq_values[i] = simulate_trial(games, rng)
    return chi_sq_values

def calculate_corrected_p(
    simulated_chi_sq: np.ndarray, 
    trial: int | None = None
) -> float:
    observed, _ = calculate_chi_square(trial)
    corrected_p = (
        (np.sum(simulated_chi_sq >= observed) + 1) / (len(simulated_chi_sq) + 1)
    )
    return corrected_p

def calculate_cohen_w(
    simulated_chi_sq: np.ndarray, 
    trial: int | None = None
) -> dict:
    df = summarize_trials()
    if trial is None:
        observations = int(df["observations"].sum())
        observed, _ = calculate_chi_square()
    else:
        observations = int(df.loc[df["trial"] == trial, "observations"].iloc[0])
        observed, _ = calculate_chi_square(trial)
    w_simulated = np.sqrt(simulated_chi_sq / observations)
    w_observed = np.sqrt(observed / observations)
    w_null_mean = np.mean(w_simulated)
    w_null_sd = np.std(w_simulated, ddof=1)
    z_w = (w_observed - w_null_mean) / w_null_sd
    percentile = np.mean(w_simulated <= w_observed) * 100
    
    return {
        "w_observed": w_observed,
        "w_null_mean": w_null_mean,
        "w_null_sd": w_null_sd,
        "z_w": z_w,
        "percentile": percentile,
    }