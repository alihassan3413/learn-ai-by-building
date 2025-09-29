import numpy as np

# Scalar arithmetic operations = When you do math with a single number, NumPy applies it to every element of the array automatically.
a = np.array([1, 2, 3])

print(a + 2)
print(a - 2)
print(a * 2)
print(a / 2)
print(a ** 2)

# Vector arithmetic operations = When you do math with two arrays, NumPy does the math element by element.

b = np.array([4, 5, 6])
c = np.array([7, 8, 9])

print(b + c)
print(b - c)
print(b * c)
print(b / c)
print(b ** c)

print("Square root of array a:", np.sqrt(a))
print("Exponential of array a:", np.exp(a))

radii = np.array([1, 2, 3])
areas = np.pi * radii**2
print("Areas of circles with given radii:", areas)

# Element wise operations = NumPy allows you to perform operations on arrays of different shapes and sizes, as long as they are compatible for broadcasting.
# Broadcasting = how NumPy handles different shapes when doing element-wise operations.
e = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
f = np.array([[4, 5, 6], [7, 8, 9], [1, 2, 3]])

print(e + f)

# Comparison operations = You can compare arrays element by element using comparison operators. The result is a boolean array indicating the outcome of each comparison.
scores = np.array([85, 90, 78, 92, 88])
print(scores > 80)
print(scores < 90)
print(scores == 88)
print(scores != 78)
print(scores >= 85)
