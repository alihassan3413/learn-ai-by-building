import numpy as np

# Filtering arrays = You can filter elements in an array based on conditions, resulting in a new array containing only the elements that meet the criteria.
data = np.array([10, 15, 20, 25, 30, 35, 40])
filtered_data = data[data > 20]
print("Filtered data (elements > 20):", filtered_data)

# for preserving original array shape after filtering use np.where
adults = np.where(data >= 18, data, 0)
print("Adults (18 and older):", adults)