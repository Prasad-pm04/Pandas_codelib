#--Date,Product,Price,Quantity
2025-06-01,Laptop,60000,3
2025-06-01,Mouse,500,10
2025-06-02,Laptop,60000,1
2025-06-02,Keyboard,1500,5
2025-06-03,Mouse,500,7



import pandas as pd

# Load the data
df = pd.read_csv("sales_data.csv")

# Add a new column 'Total' = Price * Quantity
df['Total'] = df['Price'] * df['Quantity']

# Total sales per product
total_sales = df.groupby('Product')['Total'].sum()

# Product with the highest revenue
top_product = total_sales.idxmax()
top_revenue = total_sales.max()

# Revenue per day
daily_sales = df.groupby('Date')['Total'].sum()

# Display results
print("Total Sales per Product:")
print(total_sales)

print(f"\nTop Selling Product: {top_product} with revenue ₹{top_revenue}")

print("\nTotal Revenue per Day:")
print(daily_sales)



Output :- Total Sales per Product:
Keyboard     7500
Laptop     240000
Mouse        8500

Top Selling Product: Laptop with revenue ₹240000

Total Revenue per Day:
2025-06-01    183000
2025-06-02     82500
2025-06-03      3500

