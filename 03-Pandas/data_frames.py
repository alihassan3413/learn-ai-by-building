import pandas as pd

df = pd.DataFrame([
    {"policy_id": 1, "carrier": "TypTap", "premium": 450.0, "state": "FL", "start": "2025-01-01"},
    {"policy_id": 2, "carrier": "Slide",  "premium": 1200.0, "state": "FL", "start": "2025-02-15"},
    {"policy_id": 3, "carrier": "Lemonade", "premium": 1300.0, "state": "FL", "start": "2025-03-10"},
    {"policy_id": 4, "carrier": "TypTap", "premium": 1600.0, "state": "CA", "start": "2025-01-20"},
    {"policy_id": 5, "carrier": "Slide",  "premium": 1100.0, "state": "CA", "start": "2025-02-25"},
    {"policy_id": 6, "carrier": "Lemonade", "premium": 1250.0, "state": "CA", "start": "2025-03-15"},
    {"policy_id": 8, "carrier": "Slide",  "premium": 2150.0, "state": "TX", "start": "2025-02-28"},
    {"policy_id": 7, "carrier": "TypTap", "premium": 1550.0, "state": "TX", "start": "2025-01-30"},
    {"policy_id": 9, "carrier": "Lemonade", "premium": 1350.0, "state": "TX", "start": "2025-03-20"},
])

print("DataFrame:\n", df)

print(df.head()) # return first 5 rows
print(df.tail()) # return last 5 rows
print("DataFrame Info:")
print(df.info()) # summary (types, nulls)

print("Descriptive Statistics:\n", df.describe())  # stats (mean, std, etc.)

print(df['premium'])  # single column
print(df[['policy_id', 'premium']])  # multiple columns

filtered = df['state'] == 'FL'
print("Filtered DataFrame (state == 'FL'):\n", df[filtered])

filtered_prem = df['premium'] > 1300
print("Filtered DataFrame (premium > 1300):\n", df[filtered_prem])

df['is_high_premium'] = df['premium'] > 1300
print("DataFrame with new column 'is_high_premium':\n", df)

sales = pd.DataFrame({
    "city": ["Lahore", "Karachi", "Lahore", "Karachi"],
    "amount": [200, 150, 300, 100]
})

sales_summary = sales.groupby('city')["amount"].sum()
print("Sales summary by city:\n", sales_summary)

orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4],
    "user": ["Ali", "Sara", "Ali", "Usman"],
    "amount": [250, 400, 150, 500],
    "status": ["delivered", "pending", "delivered", "delivered"]
})

total_spent = orders.groupby('user')['amount'].sum()
print(total_spent)

delivered_orders = orders[orders["status"] == 'delivered']
print(delivered_orders)

avg_amount = orders["amount"].mean()
print(avg_amount)

avg_premium = df.groupby('state')['premium'].mean()
print("Average premium by state:\n", avg_premium)


carrier = df.loc[df.groupby('state')['premium'].idxmax(), ['state', 'carrier']]
print("Max carrier by state:\n", carrier)

# Trend of policy start dates by month
df['start'] = pd.to_datetime(df['start'])
df["month"] = df["start"].dt.month
print("Policy start month trend:\n", df.groupby('month').size())