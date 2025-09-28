import pandas as pd

data_frame = pd.read_csv("./files/Walmart_Sales.csv")

# just to get info about the data
print(data_frame.head())
print(data_frame.info())
print(data_frame.describe())

# get all the columns
print(data_frame.columns)

# check missing values
print(data_frame.isnull().sum())

# Task 1
weekly_sales = data_frame.groupby('Store')['Weekly_Sales'].mean()

highest_avg_store = weekly_sales.idxmax()
highest_avg_value = weekly_sales.max()

lowest_avg_store = weekly_sales.idxmin()
lowest_avg_value = weekly_sales.min()

overall_avg = data_frame["Weekly_Sales"].mean()

print("Best Performing Store:", highest_avg_store, "->", highest_avg_value)
print("Store with lowest average weekly sales:", lowest_avg_store, "->", lowest_avg_value)
print("Overall average weekly sales across all stores:", overall_avg)

# Task 2

avg_weekly_sale = data_frame.groupby("Holiday_Flag")["Weekly_Sales"].mean()
print(avg_weekly_sale)

max_weekly_sale_holiday = data_frame.groupby("Holiday_Flag")["Weekly_Sales"].max()
print(max_weekly_sale_holiday)

max_weekly_sale_holiday = data_frame[data_frame["Holiday_Flag"] == 1].max()
print(max_weekly_sale_holiday)

# Task 3
# 🔹 3. Trends Over Time

# Convert Date column to datetime (pd.to_datetime).

data_frame["Date"] = pd.to_datetime(data_frame["Date"], dayfirst=True)
print(data_frame.head())

# Create a Month column from Date.
data_frame["Month"] = data_frame["Date"].dt.month
print(data_frame.head())

# Extract Year and Month
data_frame["YearMonth"] = data_frame["Date"].dt.to_period("M")
print(data_frame.head(3))

# Find the total sales per month across all stores.
monthly_sales = data_frame.groupby("YearMonth")["Weekly_Sales"].sum()
print(monthly_sales)

monthly_sales_per_store = data_frame.groupby(["Store", "YearMonth"])["Weekly_Sales"].sum()
print(monthly_sales_per_store.head(48))

months_per_store = data_frame.groupby("Store")["Month"].nunique()
print(months_per_store)


# Which month had the highest sales?
print(monthly_sales.idxmax(), monthly_sales.max())


# # 🔹 4. External Factors

# # Find the correlation between Weekly_Sales and:

# Temperature
temp_sales_corr = data_frame["Weekly_Sales"].corr(data_frame["Temperature"])
if temp_sales_corr > 0:
    print("⬆️ Sales increases with temprature decreases: ", temp_sales_corr )
elif temp_sales_corr < 0:
    print("⬇️ Sales decreases with temprature increases: ", temp_sales_corr)
# Fuel_Price
fuel_sales_cor = data_frame["Weekly_Sales"].corr(data_frame["Fuel_Price"])
if fuel_sales_cor > 0:
    print("⬆️ Sales increases with fuel decreases: ", fuel_sales_cor )
elif fuel_sales_cor < 0:
    print("⬇️ Sales decreases with fuel increases: ", fuel_sales_cor)
# CPI
cpi_sales_corr = data_frame["Weekly_Sales"].corr(data_frame["CPI"])
if cpi_sales_corr > 0:
    print("⬆️ Sales increases with CPI decreases: ", cpi_sales_corr)
elif cpi_sales_corr < 0:
    print("⬇️ Sales decreases with CPI increases: ", cpi_sales_corr)
# Unemployment
unemployment_sales_corr = data_frame["Weekly_Sales"].corr(data_frame["Unemployment"])
if unemployment_sales_corr > 0:
    print("⬆️ Sales increases with unemployment decreases: ", unemployment_sales_corr)
elif unemployment_sales_corr < 0:
    print("⬇️ Sales decreases with unemployment increases: ", unemployment_sales_corr)

# Which factor seems most related to sales?
# Factor with highest absolute correlation value
factors_corr = {
    "Temperature": abs(temp_sales_corr),
    "Fuel_Price": abs(fuel_sales_cor),
    "CPI": abs(cpi_sales_corr),
    "Unemployment": abs(unemployment_sales_corr)
}
most_related_factor = max(factors_corr, key=factors_corr.get)
print("Most related factor to sales:", most_related_factor, "with correlation:", factors_corr[most_related_factor])

5. Advanced (if you want a challenge 🚀)

# Find the top 3 stores with the most consistent sales (lowest standard deviation in Weekly_Sales).
consistent_stores = data_frame.groupby("Store")["Weekly_Sales"].std().nsmallest(3)
print("Top 3 stores with most consistent sales:\n", consistent_stores)

# Find the yearly trend of sales (group by year).
data_frame["Year"] = data_frame["Date"].dt.year
yearly_sales = data_frame.groupby("Year")["Weekly_Sales"].sum()
print("Yearly sales trend:\n", yearly_sales)
