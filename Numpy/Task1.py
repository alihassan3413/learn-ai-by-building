# Task 1: Create & Reshape

# Create a NumPy array with numbers from 1 to 20 and reshape it into a 4x5 matrix.

# Then extract the second row and the third column.

import numpy as np

arr = np.arange(1, 21)

newarr = arr.reshape(4, 5)

print(newarr)

sec_row = newarr[1, :]

print("Second row:", sec_row)

third_col = newarr[:, 2]
print("Third column:", third_col)