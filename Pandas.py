import pandas as pd
data = pd.read_csv("Project ecommerce_sales_data/ecommerce_sales_data(2).csv")

print(data.head(5))
print(data.describe())
print(data.shape)
print(data.info())
print(data.tail())


print(data.dropna())
print(data.duplicated())
print(data.isnull())




