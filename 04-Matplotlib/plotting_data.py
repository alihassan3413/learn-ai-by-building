import matplotlib.pyplot as plt
import numpy as np

x_data = np.random.random(50)*100
y_data = np.random.random(50)*100

# plt.scatter(x_data, y_data)
# plt.show()

years = [2006 + x for x in range(20)]
weights = [80, 83, 85, 90, 92, 95, 97, 100, 102, 105, 107, 110, 112, 115, 117, 120, 122, 125, 127, 130]

print(len(years), len(weights))

plt.plot(years, weights)
plt.show()


