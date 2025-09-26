# Task 3: Matrix Operations

# Generate two random 3x3 matrices (integers between 1 and 10).

# Perform matrix multiplication (not elementwise).

# Also find the transpose of the result.

import numpy as np

arr1 = np.arange(1, 10).reshape(3, 3)
arr2 = np.arange(1, 10).reshape(3, 3)

print("Array 1:\n", arr1)
print("Array 2:\n", arr2)

#( Matrix multiplication with element wise)
# arr = arr1 * arr2

arr = np.matmul(arr1, arr2)
print("Product of both arrays:\n", arr)

arr_t = arr.transpose()
print("Transposed array:\n", arr_t)