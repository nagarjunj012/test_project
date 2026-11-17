import pandas as pd
import matplotlib.pyplot as plt


sales = pd.read_csv("data/sales.csv")

# Calculate revenue for each sale
sales["revenue"] = sales["units_sold"] * sales["unit_price"]

print("Sales with revenue:")
print(sales[["order_id", "product", "units_sold", "unit_price", "revenue"]])

# Calculate total revenue
total_revenue = sales["revenue"].sum()
print("\nTotal revenue:", total_revenue)

# Calculate revenue by product
revenue_by_product = sales.groupby("product")["revenue"].sum()
print("\nRevenue by product:")
print(revenue_by_product)

# Calculate revenue by region
revenue_by_region = sales.groupby("region")["revenue"].sum()
print("\nRevenue by region:")
print(revenue_by_region)

# Calculate revenue by category
revenue_by_category = sales.groupby("category")["revenue"].sum()
print("\nRevenue by category:")
print(revenue_by_category)

# Convert order_date from text to dates
sales["order_date"] = pd.to_datetime(sales["order_date"])

# Create a year-month value for grouping
sales["month"] = sales["order_date"].dt.to_period("M")

# Calculate revenue by month
revenue_by_month = sales.groupby("month")["revenue"].sum()
print("\nRevenue by month:")
print(revenue_by_month)

revenue_by_product = sales.groupby("product")["revenue"].sum()
revenue_by_product = revenue_by_product.sort_values(ascending=False)

revenue_by_product.plot(kind="bar", color="steelblue")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

print("\nRevenue by product (highest to lowest):")
print(revenue_by_product)