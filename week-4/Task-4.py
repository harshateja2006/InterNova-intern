# Task 4: Outlier Detection
# Using a numerical dataset:
# 1. Identify potential outliers.
# 2. Use an appropriate method to detect outliers.
# 3. Display the identified outliers.
# 4. Explain how outliers can affect data analysis.

import numpy as np

sales = [20, 22, 24, 25, 23, 26, 28, 24, 27, 25, 100]

q1 = np.percentile(sales, 25)
q3 = np.percentile(sales, 75)

iqr = q3 - q1

lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr

outliers = [
    value for value in sales
    if value < lower_limit or value > upper_limit
]

print("Sales Data:", sales)
print("First Quartile (Q1):", round(q1, 2))
print("Third Quartile (Q3):", round(q3, 2))
print("Interquartile Range (IQR):", round(iqr, 2))
print("Lower Limit:", round(lower_limit, 2))
print("Upper Limit:", round(upper_limit, 2))
print("Identified Outliers:", outliers)

print("\nExplanation:")
print("The IQR method identifies values outside the lower and upper limits as potential outliers.")
print("The value 100 is unusually high compared with the other sales values, so it is identified as an outlier.")
print("Outliers can affect the mean, standard deviation, and conclusions drawn from data analysis.")
