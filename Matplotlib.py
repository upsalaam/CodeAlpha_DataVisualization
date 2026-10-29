import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Project ecommerce_sales_data/ecommerce_sales_data(2).csv")
region_sales = data.groupby("Region")["Sales"].sum()


fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# Chart 1: Sales by Region
region_sales.plot(kind="bar", ax=ax[0, 0])
ax[0, 0].set_title("Sales by Region")

data["Order Date"] = pd.to_datetime(data["Order Date"])

data["Month"] = data["Order Date"].dt.to_period("M")

monthly_sales = data.groupby("Month")["Sales"].sum()


# Chart 2: Monthly Sales
monthly_sales.plot(kind="line", marker="o", ax=ax[0, 1])
ax[0, 1].set_title("Monthly Sales Trend")

# chart 3: Sales vs QUantity
data.plot(
    kind="scatter",
    x="Quantity",
    y="Sales",
    ax=ax[1, 0]
)
ax[1, 0].set_title("Sales vs Quantity")
ax[1, 0].set_xlabel("Quantity")
ax[1, 0].set_ylabel("Sales")


category_sales = data.groupby("Category")["Sales"].sum()

category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")


plt.tight_layout()
plt.show()

# Business insights
print("Sales by Region:")
print(data.groupby("Region")["Sales"].sum().sort_values(ascending=False))

print("\nSales by Product:")
print(data.groupby("Product Name")["Sales"].sum().sort_values(ascending=False))


# show the top 3 product_sales
product_sales = (
    data.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(product_sales.head(3))

# chech for data
print("Missing values:")
print(data.isnull().sum())

print("Duplicate rows:", data.duplicated().sum())
