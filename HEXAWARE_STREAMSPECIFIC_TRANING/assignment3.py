import pandas as pd

#1. Load Data and Display Info
df = pd.read_csv('Superstore.csv')
print(f"Shape: {df.shape}")
print("Data Types:\n", df.dtypes)

#2. Clean Column Names & Normalize Dates
df.columns = df.columns.str.replace(r'[/\s]+', '_', regex=True)
df['Order_Date'] = pd.to_datetime(df['Order_Date'], dayfirst=True)
df['Ship_Date'] = pd.to_datetime(df['Ship_Date'], dayfirst=True)

#3. Profitability by Region and Category
profit_summary = df.groupby(['Region', 'Category']).agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Discount': 'mean'
}).reset_index()
most_profitable = profit_summary.loc[profit_summary['Profit'].idxmax()]
print("Most Profitable Region + Category:\n", most_profitable)

#4. Top 5 Most Profitable Products
top_products = df.groupby('Product_Name')['Profit'].sum().sort_values(ascending=False).head(5)
print("Top 5 Profitable Products:\n", top_products)

#5. Monthly Sales Trend
df['Month'] = df['Order_Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()
print("Monthly Sales Trend:\n", monthly_sales)

#6. Cities with Highest Average Order Value
df['Order_Value'] = df['Sales'] / df['Quantity']
city_order_value = df.groupby('City')['Order_Value'].mean().sort_values(ascending=False).head(10)
print("Top Cities by Avg Order Value:\n", city_order_value)

#7. Save Loss-Making Orders
loss_orders = df[df['Profit'] < 0]
loss_orders.to_csv('loss_orders.csv', index=False)
print(f"Saved {len(loss_orders)} loss-making orders to 'loss_orders.csv'")

#8. Detect Nulls & Impute Price if Exists
null_counts = df.isnull().sum()
print("🔍 Null Values:\n", null_counts[null_counts > 0])

if 'Price' in df.columns:
    df['Price'] = df['Price'].fillna(1)
    print("'Price' column missing values filled with 1")
