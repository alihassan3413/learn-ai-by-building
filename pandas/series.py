import pandas as pd
import numpy as np

calories = {'Day 1': 450, 'Day 2': 500, 'Day 3': 600}

calories_series = pd.Series(calories)
print(calories_series)

first_element = calories_series.iloc[0]
first_ele = calories_series.loc['Day 1']
print("First element:", first_element)
print("First element using loc:", first_ele)

last_element = calories_series.iloc[-1]
print("Last element:", last_element)

sliced_series = calories_series[0:2]
print("Sliced series (first two days):")
print(sliced_series)

arr = np.random.randint(1, 101, 10)
arr_series = pd.Series(arr)
print("Original series:\n", arr_series)

arr_s = pd.Series([3, 5, 7, 9, 11])
print("Filtered series (values > 5):\n", arr_s[arr_s > 5])

duplicate_series = pd.Series([1, 2, 2, 3, 4, 4, 5])
unique_series = duplicate_series.drop_duplicates()
print("Unique values in the series:\n", unique_series)
print("Count of unique values:", duplicate_series.value_counts())

date_range = pd.Series(pd.date_range(start='2025-01-01', periods=7))
print("Date range series:\n", date_range)

series_1 = pd.Series([1, 2, 3, 4, 5])
series_2 = pd.Series([10, 20, 30, 40, 50])

print("Element-wise addition:\n", series_1 + series_2)
print("Element-wise subtraction:\n", series_1 - series_2)   
print("Element-wise multiplication:\n", series_1 * series_2)
print("Element-wise division:\n", series_1 / series_2)

series_with_nan = pd.Series([1, 2, np.nan, 4, 5, np.nan])
print("Original series with NaN values:\n", series_with_nan)

mean_value = series_with_nan.mean()
filled_series = series_with_nan.fillna(mean_value)
print("Series after filling NaN with mean value:\n", filled_series)