# Task 2: Border & Inside

# Create a 6x6 matrix of all 1s.

# Set the border elements to 0 but keep the inside as 1.

import numpy as np

arr = np.ones((6, 6), dtype=int)
print("Original array:\n", arr)

arr[:, 0] = 0
arr[0, :] = 0
arr[-1, :] = 0
arr[:, -1] = 0

print("Modified array:\n", arr)