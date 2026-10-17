# Task 6: Seaborn Visualization
# Using a suitable dataset, create the following visualizations:
# 1. Count Plot
# 2. Box Plot
# 3. Heatmap
# 4. Pair Plot
#
# For each visualization:
# 1. Add an appropriate title.
# 2. Use relevant variables.
# 3. Display the output.
# 4. Briefly explain the pattern or relationship shown.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Department": ["IT", "HR", "IT", "Sales", "HR",
                   "IT", "Sales", "Finance", "Finance", "Sales"],
    "Salary": [55000, 42000, 68000, 62000, 45000,
               75000, 59000, 48000, 51000, 65000],
    "Experience": [2, 1, 4, 3, 2, 5, 3, 2, 3, 4],
    "Performance": [4, 3, 5, 4, 3, 5, 4, 3, 4, 5]
})

sns.countplot(data=data, x="Department")
plt.title("Employee Count by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.show()

print("Count Plot: Shows the number of employees in each department.")

sns.boxplot(data=data, x="Department", y="Salary")
plt.title("Salary Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.tight_layout()
plt.show()

print("Box Plot: Compares salary distributions across departments and helps identify potential outliers.")

correlation = data[["Salary", "Experience", "Performance"]].corr()

sns.heatmap(correlation, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

print("Heatmap: Shows the strength and direction of relationships between numerical variables.")

sns.pairplot(data, vars=["Salary", "Experience", "Performance"], hue="Department")
plt.suptitle("Pair Plot of Employee Data", y=1.02)
plt.show()

print("Pair Plot: Compares pairs of numerical variables and shows patterns across departments.")
