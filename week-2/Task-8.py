"""Merge, Concatenate, GroupBy & Pivot Table
Using two or more datasets, perform the following operations:

Merge & Concatenate
Merge two DataFrames using a common column.
Concatenate two DataFrames.
GroupBy
Group data based on a selected column.
Calculate aggregate values such as sum, mean, count, minimum, or maximum.
Pivot Table
Create a Pivot Table using Pandas.
Summarize the data based on appropriate rows, columns, and values."""

import pandas as pd

df = pd.read_csv("sales_data.csv")

print("Original Dataset:")
print(df)

product_info = pd.DataFrame({
    "Product": ["Laptop", "Smartphone", "Headphones", "Keyboard", "Monitor"],
    "Brand": ["Dell", "Samsung", "Sony", "Logitech", "LG"]
})

print("\nProduct Information:")
print(product_info)

merged_df = pd.merge(df, product_info, on="Product")

print("\nMerged Dataset:")
print(merged_df)

part1 = df.iloc[:3]
part2 = df.iloc[3:]

concatenated_df = pd.concat([part1, part2])

print("\nConcatenated Dataset:")
print(concatenated_df)

print("\nGroupBy Category:")
print(df.groupby("Category")["Total_Sales"].sum())

print("\nGroupBy City:")
print(df.groupby("City")["Total_Sales"].sum())

pivot_table = pd.pivot_table(
    df,
    values="Total_Sales",
    index="Category",
    columns="Payment",
    aggfunc="sum",
    fill_value=0
)

print("\nPivot Table:")
print(pivot_table)