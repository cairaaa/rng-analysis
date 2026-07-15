# Evaluating the Randomness of a Minigame Selection System

> A statistical research project investigating whether the selection in a video
> game follows a uniform distribution, using chi-square goodness of fit testing,
> Monte Carlo simulations, and effect size analysis on 3,300+ real games of
> collected data.

## Overview 

Players have long speculated that certain minigames in a video game are selected
more often than others. This project tests that claim across 10 independent
trials (3,318 total games, 26,544 individual minigame selections), checking
whether the observed selection frequencies are consistent with a truly uniform
random process. Exploratory analyses were also performed to discover whether
slot position or time had an effect on the minigame selection.

**Read the full paper:** [PDF](paper/rng-analysis.pdf) · [Web version](https://cairaaa.github.io/rng-analysis/)

## Key findings

* There was no evidence of bias within the combined dataset (Monte
  Carlo–corrected *p* = 0.1676), along with a negligible effect size (Cohen's
  *w* = 0.0293, 83.24th percentile of the null distribution)
* When looking at the individual trials, none of them showed a significant
  deviation (corrected *p* range: 0.078–0.666), ruling out the possibility that
  the combined result was masking an anomalous trial
* The exploratory analysis revealed a statistically significant but practically
  negligible association between slot position and minigame selection (Cramér's
  *V* = 0.0346), likely due to the large sample size rather than real bias
* Therefore, the minigame selection system behaves consistently with genuine
  randomness

## Methodology

* The primary and secondary tests used chi-square goodness of fit tests against
  the null hypothesis, which suggested that each minigame had an equal chance of
  being selected (1/26)
* The Monte Carlo simulation (100,000 iterations, seed = 42) was used to correct
  the dependent observations, since 8 minigames are selected from a pool of 26
  minigames without replacement
  * These values were used in order to generate the corrected p value along with
    the effect size
* Cohen's *w* was used to calculate the effect size; since Cohen's *w* assumes
  independence, the effect size was reported as a percentile to the values
  generated from the Monte Carlo simulation
* The exploratory analyses used the chi-square tests of independence (with
  Cramér's *V*) to examine whether slot position or hour of day are correlated
  with minigame selection

Full statistical detail and formulas are in Section 2 of the paper.

## Data

Data were collected across 10 independent trials (322–342 games each), for a
total of 3,318 games after removing 44 incomplete/misrecorded records. Each row
in the processed dataset represents one minigame selection, with columns:
`trial`, `game_number`, `slot` (1–8), `timestamp`, and `minigame`.

Full details are found in Section 2.2 of the paper.

## License

**Code:** Licensed under the MIT license

**Paper:** Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
