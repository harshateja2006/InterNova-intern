"""Selecting, Filtering & Sorting Data
Using a Pandas DataFrame:

Select specific columns.
Select specific rows.
Filter records based on a condition.
Apply multiple filtering conditions.
Sort data in ascending order.
Sort data in descending order."""
import pandas as pd

df = pd.read_csv("sales_data.csv")

print("Complete Dataset:")
print(df)

print("\nSelected Columns:")
print(df[["Customer", "Product", "Total_Sales"]])

print("\nSelected Rows:")
print(df.iloc[0:3])

print("\nSales Greater Than 10000:")
print(df[df["Total_Sales"] > 10000])

print("\nElectronics Products:")
print(df[df["Category"] == "Electronics"])

print("\nElectronics With Sales Greater Than 30000:")
print(df[(df["Category"] == "Electronics") & (df["Total_Sales"] > 30000)])

print("\nSorted by Total Sales - Ascending:")
print(df.sort_values("Total_Sales"))

print("\nSorted by Total Sales - Descending:")
print(df.sort_values("Total_Sales", ascending=False))