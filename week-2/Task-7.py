"""Handling Missing Values (10 Marks)

Take a dataset containing missing values and perform the following:

Identify missing values using isnull() / isna().
Count missing values in each column.
Remove rows containing missing values.
Fill missing values using appropriate methods.
Display the dataset before and after handling missing values."""
import pandas as pd

df = pd.read_csv("sales_data.csv")

df.loc[1, "City"] = None
df.loc[3, "Payment"] = None

print("Dataset With Missing Values:")
print(df)

print("\nMissing Values:")
print(df.isnull())

print("\nNumber of Missing Values:")
print(df.isnull().sum())

df_dropped = df.dropna()

print("\nAfter Dropping Missing Rows:")
print(df_dropped)

df["City"] = df["City"].fillna("Unknown")
df["Payment"] = df["Payment"].fillna("Unknown")

print("\nAfter Filling Missing Values:")
print(df)

print("\nFinal Missing Value Count:")
print(df.isna().sum())