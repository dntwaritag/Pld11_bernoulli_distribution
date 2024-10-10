## JOHN AKECH

# Importing libraries:

import numpy as np  # For numerical computations
import matplotlib.pyplot as plt  # Foror plotting graphs
from scipy.stats import binom  # Importing binom from scipy for binomial distribution-related functions

# Parameters for the Bernoulli distribution
p = 0.60  # Probability of scoring a goal (success), e.g., a player makes a shot 60% of the time
q = 1 - p  # Probability of missing the goal (failure), which is 1 minus the probability of success (here 40%)

# Simulate the outcomes of penalty kicks
num_trials = 10000  # Number of simulated penalty kicks
penalty_kicks = np.random.binomial(1, p, num_trials)

# Calculate probabilities of scoring (1) and missing (0)
goals = np.sum(penalty_kicks == 1) / num_trials
misses = np.sum(penalty_kicks == 0) / num_trials

