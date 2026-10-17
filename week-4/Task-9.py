# Task 9: Business Recommendations
# Based on EDA and findings:
# 1. Provide at least 2 data-driven business recommendations.
# 2. Explain how the recommendations are supported by the data.

import pandas as pd

data = {
    "Employee": ["Rahul", "Priya", "Arjun", "Sneha", "Kiran",
                 "Divya", "Anjali"],
    "Department": ["IT", "HR", "IT", "Finance", "IT", "Sales", "Sales"],
    "Salary": [55000, 42000, 68000, 50000, 75000, 50000, 62000],
    "Experience": [2, 1, 4, 3, 5, 2, 3],
    "Performance": [3, 3, 5, 4, 5, 4, 4]
}

df = pd.DataFrame(data)

print("EMPLOYEE DATA SUMMARY")
print("Average Salary:", round(df["Salary"].mean(), 2))
print("Average Experience:", round(df["Experience"].mean(), 2))
print("Average Performance:", round(df["Performance"].mean(), 2))

print("\nBUSINESS RECOMMENDATIONS")

print("\n1. Provide Training and Development")
print("Recommendation: Offer training and skill development")
print("programs to employees with lower performance scores.")
print("Data Support: Employees with lower performance scores can be identified for additional support and training.")

print("\n2. Review Salary and Career Progression")
print("Recommendation: Review salary ranges and career growth opportunities based on experience, performance, and role.")
print("Data Support: The dataset contains differences in salary,experience, and performance across employees.")

print("\nConclusion:")
print("Data analysis helps organizations identify patterns, support decisions, and improve employee development.")
print("These recommendations should be validated using a larger real-world dataset before implementation.")
