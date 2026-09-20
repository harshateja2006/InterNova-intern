"""Mini Data Analysis Project
Perform a basic data analysis project using NumPy and Pandas.

Choose a dataset such as:

Student Performance Dataset
Sales Dataset
Employee Dataset
E-commerce Dataset
Customer Dataset"""

import pandas as pd

df = pd.read_csv("sales_data.csv")

print("Dataset:")
print(df)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSelected Columns:")
print(df[["Customer", "Product", "Total_Sales"]])

print("\nSales Greater Than 10000:")
print(df[df["Total_Sales"] > 10000])

print("\nSorted Sales:")
print(df.sort_values("Total_Sales", ascending=False))

print("\nTotal Sales by Category:")
print(df.groupby("Category")["Total_Sales"].sum())

print("\nTotal Sales by City:")
print(df.groupby("City")["Total_Sales"].sum())

pivot = pd.pivot_table(
    df,
    values="Total_Sales",
    index="Category",
    columns="Payment",
    aggfunc="sum",
    fill_value=0
)

print("\nPivot Table:")
print(pivot)

df.to_csv("cleaned_sales_data.csv", index=False)

print("\nCleaned dataset exported successfully.")