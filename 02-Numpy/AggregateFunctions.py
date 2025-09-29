import numpy as np

arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10]])

print("Sum of all elements:", np.sum(arr))
print("Mean of all elements:", np.mean(arr))
print("Max of all elements:", np.max(arr))
print("Min of all elements:", np.min(arr))
print("Standard Deviation of all elements:", np.std(arr))
print("Variance of all elements:", np.var(arr))

print("Sum along columns:", np.sum(arr, axis=0))
print("Sum along rows:", np.sum(arr, axis=1))
print("Mean along columns:", np.mean(arr, axis=0))
print("Mean along rows:", np.mean(arr, axis=1))