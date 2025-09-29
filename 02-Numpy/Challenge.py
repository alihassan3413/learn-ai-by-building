import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

print("Original array:", arr)

reshape = arr.reshape(4,5)
print("Reshaped array (4x5):")
print(reshape)

print("Slicing 2nd row: ", reshape[1:2, :])
print("Last column: \n", reshape[:, -1:])

print(reshape[1:3, 1:3])

rand_matrix1 = np.random.randint(1,11, size=(3,3))
rand_matrix2 = np.random.randint(1,11, size=(3,3))
print("Random matrix (3x3):")
print(rand_matrix1)
print("Random matrix (3x3):")
print(rand_matrix2)

print("Element-wise addition:\n", rand_matrix1 + rand_matrix2)
print("Element-wise subtraction:\n", rand_matrix1 - rand_matrix2)
print("Element-wise multiplication:\n", rand_matrix1 * rand_matrix2)

print("Matrix multiplication:\n", np.matmul(rand_matrix1, rand_matrix2))

arr = np.random.randint(1, 101, 100)
print("Original array:", arr)
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Sum:", np.sum(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))

filtered = arr[arr > 50]
print("Filtered (values > 50):", filtered)

# count how many are even
even = arr[arr % 2 == 0]
print("Count (even values):", even.size)