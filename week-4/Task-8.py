# Task 8: EDA – Correlation & Insights
# Continue the analysis of the selected dataset:
# 1. Perform correlation analysis.
# 2. Identify important relationships between variables.
# 3. Identify patterns and trends.
# 4. Use appropriate visualizations.
# 5. Write at least 3 meaningful insights.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Employee": ["Rahul", "Priya", "Arjun", "Sneha", "Kiran",
                 "Divya", "Anjali"],
    "Department": ["IT", "HR", "IT", "Finance", "IT", "Sales", "Sales"],
    "Salary": [55000, 42000, 68000, 50000, 75000, 50000, 62000],
    "Experience": [2, 1, 4, 3, 5, 2, 3],
    "Performance": [3, 3, 5, 4, 5, 4, 4]
}

df = pd.DataFrame(data)

print("DATASET")
print(df)

correlation = df[["Salary", "Experience", "Performance"]].corr()

print("\nCORRELATION MATRIX")
print(correlation.round(2))

sns.heatmap(correlation, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Employee Data Correlation Heatmap")
plt.tight_layout()
plt.show()

sns.scatterplot(data=df, x="Experience", y="Salary", hue="Department")
plt.title("Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.tight_layout()
plt.show()

print("\nINSIGHTS")

print("1. Salary generally increases with experience in this dataset.")

print("2. Employees with higher performance scores tend to have higher salaries in this sample.")

print("3. Salary and experience show a positive relationship, suggesting that more experienced employees may earn more.")

print("4. Salary varies across employees and departments.")

print("\nNote: These are patterns in the sample data and do not prove that experience or performance causes higher salary.")
