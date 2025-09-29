import numpy as np

rng = np.random.default_rng(seed=1)

print(rng.random())  # Random float in [0.0, 1.0)
print(rng.integers(1, 10, size=(3, 3)))  # Random integer in [1, 10) 