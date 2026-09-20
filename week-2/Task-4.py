"""Pandas Series & DataFrame
Create a Pandas program that:

Creates a Pandas Series.
Creates a DataFrame containing student or employee information.
Displays the DataFrame.
Displays the column names.
Displays the index.
Adds a new column to the DataFrame.
Displays the updated DataFrame."""

import pandas as pd

series = pd.Series([85, 90, 78, 92, 88])

print("Pandas Series:")
print(series)

data = {
    "Name": ["Harsha", "Rahul", "Priya", "Arjun", "Sneha"],
    "Branch": ["CSD", "CSE", "ECE", "CSD", "CSE"],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)

print("\nStudent DataFrame:")
print(df)

print("\nColumn Names:")
print(df.columns)

print("\nIndex:")
print(df.index)

df["Grade"] = ["B", "A", "C", "A", "B"]

print("\nUpdated DataFrame:")
print(df)