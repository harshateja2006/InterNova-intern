"""Exporting Data
After processing the dataset:

Export the final DataFrame to a new CSV file.
Verify that the exported file contains the processed data.
Save the file properly for submission."""

import pandas as pd

df = pd.read_csv("sales_data.csv")

print("Original Dataset:")
print(df)

output_file = "final_sales_data.csv"
df.to_csv(output_file, index=False)

print("\nData exported successfully to:", output_file)

check_df = pd.read_csv(output_file)

print("\nExported Dataset:")
print(check_df)

print("\nFile Shape:")
print(check_df.shape)