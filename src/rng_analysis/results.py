import json
from pathlib import Path

from rng_analysis.analysis import (
    calculate_chi_square,
    calculate_cohen_w,
    calculate_corrected_p,
    simulate_null_distribution,
)
from rng_analysis.load import load_results


class Results:
    def __init__(self) -> None:
        self.data = load_results()

    def get(self, path: str, digits: int | None = None) -> float:
        value = self.data
        for key in path.split("."):
            value = value[key]
        value = float(value) # type: ignore
        if digits is not None:
            return round(value, digits)
        return value

results = Results()

def save_statistics() -> None:
    trials = range(1, 11)

    # per-trial stats
    results = {trial: calculate_chi_square(trial) for trial in trials}
    chi2 = {trial: result[0] for trial, result in results.items()}
    p_standard = {trial: result[1] for trial, result in results.items()}

    simulations = {trial: simulate_null_distribution(trial) for trial in trials}
    p_corrected = {
        trial: calculate_corrected_p(simulations[trial], trial) for trial in trials
    }
    cohen_w = {trial: calculate_cohen_w(simulations[trial], trial) for trial in trials}

    # combined dataset stats
    combined_chi2, combined_p_standard = calculate_chi_square()
    combined_sims = simulate_null_distribution()
    combined_p_corrected = calculate_corrected_p(combined_sims)
    combined_cohen_w = calculate_cohen_w(combined_sims)

    results = {
        "trials": {
            trial: {
                "chi_square": chi2[trial],
                "p_standard": p_standard[trial],
                "p_corrected": p_corrected[trial],
                "cohen_w": cohen_w[trial]
            }
            for trial in trials
        },
        "combined": {
            "chi_square": combined_chi2,
            "p_standard": combined_p_standard,
            "p_corrected": combined_p_corrected,
            "cohen_w": combined_cohen_w
        },
        "metadata": {
            "simulations": 100000,
            "seed": 42,
            "minigames_total": 26,
            "minigames_per_game": 8
        }
    }

    output_path = Path("data/results.json")

    with output_path.open("w") as file:
        json.dump(results, file, indent=4)

    print(f"saved results to {output_path}")