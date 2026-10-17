# Task 1: Statistical Analysis – Mean, Median & Mode
# Using a suitable numerical dataset:
# 1. Calculate the Mean.
# 2. Calculate the Median.
# 3. Calculate the Mode.
# 4. Display the results.
# 5. Briefly explain what each measure tells us about the dataset.
import numpy as np
from scipy import stats

sales = [12, 15, 18, 15, 20, 22, 15, 25, 28, 30]

mean_value = np.mean(sales)
median_value = np.median(sales)
mode_value = stats.mode(sales, keepdims=True).mode[0]

print("Sales Data:", sales)
print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)

print("Mean represents the average sales.")
print("Median represents the middle value.")
print("Mode represents the most frequent value.")
