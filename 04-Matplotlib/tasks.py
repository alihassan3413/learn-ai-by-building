import matplotlib.pyplot as plt
scores = [55, 62, 67, 70, 72, 74, 75, 77, 80, 82, 85, 88, 90, 92, 95, 100, 20, 30]

# plt.hist(scores, bins=10, edgecolor="red")
# plt.title("Histogram with 5 bins.")

# Q: Do the scores look normally distributed, skewed, or with outliers?
# The data is left skewed because of the outliers like 20,30 other than those all are towards right mostly people fall between above 60

plt.boxplot(scores)

# What are the outliers?
# Outliers are 20,30
plt.show()