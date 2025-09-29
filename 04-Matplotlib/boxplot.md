## Key Parts of a Boxplot:
# 1. **Median (Q2)** → line inside the box (middle value of data).
# 2. **Q1 (25th percentile)** → bottom of the box (25% of data lies below this). The bottom edge of the box (Q1) = the point where a quarter (25%) of your data is below.
# 3. **Q3 (75th percentile)** → top of the box (75% of data lies below this). The top edge of the box (Q3) = the point where three-quarters (75%) of your data is below.
# 4. **IQR (Interquartile Range)** = Q3 – Q1 → spread of the middle 50% of data.
# 5. **Whiskers** → lines extending from the box to show normal range:
#    - Lower whisker = lowest value ≥ (Q1 – 1.5 × IQR).
#    - Upper whisker = highest value ≤ (Q3 + 1.5 × IQR).
# 6. **Outliers** → any value outside the whiskers (plotted as dots).


## How to Read a Boxplot:
# - The **box** = where the middle 50% of the data lies.
# - The **line inside box** = median (middle of dataset).
# - The **whiskers** = "normal" minimum and maximum values.
# - The **dots outside whiskers** = outliers (unusual data points).


# scores = [55, 62, 67, 70, 72, 74, 75, 77, 80, 82, 85, 88, 90, 92, 95, 100, 20, 30]
# sort this first [20, 30, 55, 62, 67, 70, 72, 74, 75, 77, 80, 82, 85, 88, 90, 92, 95, 100]
# get its median (Q2) suppose 76
# find the median of lower half from median (76) [20, 30, 55, 62, 67, 70, 72, 74, 75]
# Q1 = 67 (median of lower half)
# find the median of the upper half from median (76) [77, 80, 82, 85, 88, 90, 92, 95, 100]
# Q3 = 88 (median of upper half)
# IQR = Q3 - Q1 = 88 - 67 = 21
# Lower whisker = lowest value ≥ (Q1 – 1.5 × IQR) = 67 - 1.5*21 = 67 - 31.5 = 35.5 → lowest value ≥ 35.5 is 55
# Upper whisker = highest value ≤ (Q3 + 1.5 × IQR) = 88 + 1.5*21 = 88 + 31.5 = 119.5 → highest value ≤ 119.5 is 100
# Outliers = any value outside the whiskers = [20, 30]