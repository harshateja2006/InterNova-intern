"""Use a CSV dataset and perform the following operations:

Read the CSV file using Pandas.
Display the first 5 rows using head().
Display the last 5 rows using tail().
Check the number of rows and columns.
Display column names.
Check data types using dtypes.
Use info() and describe() to understand the dataset."""

import pandas as pd

df = pd.read_csv("sales_data.csv")

print("First 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print("\nNumber of Rows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())