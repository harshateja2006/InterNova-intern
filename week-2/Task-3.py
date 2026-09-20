"""NumPy Mathematical & Statistical Operations
Perform the following operations using NumPy:

Mathematical Operations
Addition & Subtraction & Multiplication & Division

Statistical Functions
Mean & Median & Minimum & Maximum
Standard Deviation & Sum"""
import numpy as np

data = np.array([10, 20, 30, 40, 50])

print("Dataset:")
print(data)

print("\nMathematical Operations")
print("Addition:", data + 5)
print("Subtraction:", data - 5)
print("Multiplication:", data * 2)
print("Division:", data / 2)

print("\nStatistical Operations")
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))
print("Standard Deviation:", np.std(data))
print("Sum:", np.sum(data))