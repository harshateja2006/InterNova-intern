# Task 7: EDA – Data Inspection & Cleaning
# Data Inspection:
# 1. Check the number of rows and columns.
# 2. Display column names.
# 3. Check data types.
# 4. Generate a statistical summary.
#
# Data Cleaning:
# 5. Identify missing values.
# 6. Handle missing values appropriately.
# 7. Check for duplicate records.
# 8. Remove duplicates where required.
# 9. Check for incorrect or inconsistent values.
# 10. Display the dataset before and after cleaning.

import pandas as pd
import numpy as np

data = {
    "Employee": ["Rahul", "Priya", "Arjun", "Sneha", "Kiran",
                 "Rahul", "Divya", "Anjali"],
    "Department": ["IT", "HR", "IT", "Finance", "IT",
                   "IT", "Sales", "Sales"],
    "Salary": [55000, 42000, 68000, np.nan, 75000,
               55000, -5000, 62000],
    "Experience": [2, 1, 4, 3, 5, 2, 2, np.nan]
}

df = pd.DataFrame(data)

print("DATASET BEFORE CLEANING")
print(df)

print("\nDATA INSPECTION")
print("Number of Rows and Columns:", df.shape)
print("Column Names:", df.columns.tolist())
print("\nData Types:")
print(df.dtypes)

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nIncorrect Values:")
print(df[df["Salary"] < 0])

df = df.drop_duplicates()

df["Salary"] = df["Salary"].fillna(df["Salary"].median())
df["Experience"] = df["Experience"].fillna(df["Experience"].median())

df.loc[df["Salary"] < 0, "Salary"] = df["Salary"].median()

df["Department"] = df["Department"].str.strip().str.title()

print("\nDATASET AFTER CLEANING")
print(df)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Records After Cleaning:")
print(df.duplicated().sum())

print("\nStatistical Summary After Cleaning:")
print(df.describe())

print("\nExplanation:")
print("Data inspection helps us understand the dataset.")
print("Missing salary and experience values are replaced with their median values.")
print("Duplicate records are removed.")
print("Negative salary values are treated as invalid and replaced with the median salary.")
print("These steps improve data quality for further analysis.")
