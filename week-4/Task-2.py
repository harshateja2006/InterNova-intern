# Task 2: Variance & Standard Deviation
# Using the same or another suitable dataset:
# 1. Calculate Variance.
# 2. Calculate Standard Deviation.
# 3. Display the results.
# 4. Explain what standard deviation indicates about the spread of the data.

import numpy as np

sales = [12, 15, 18, 15, 20, 22, 15, 25, 28, 30]

variance = np.var(sales)
std_deviation = np.std(sales)

print("Sales Data:", sales)
print("Variance:", round(variance, 2))
print("Standard Deviation:", round(std_deviation, 2),"\n")

print("Variance measures the spread of data around the mean.")
print("Standard deviation indicates how far values typically")
print("deviate from the mean.")
