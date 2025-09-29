import matplotlib.pyplot as plt
import numpy as np

salaries = [35000, 37000, 39000, 42000, 45000, 47000, 49000, 52000, 54000,
            60000, 62000, 65000, 70000, 72000, 100000, 120000, 250000]

bin_range = np.arange(min(salaries), max(salaries)+10000, 10000)

plt.hist(salaries, bins=bin_range, edgecolor="red")
# plt.boxplot(salaries)
plt.show()