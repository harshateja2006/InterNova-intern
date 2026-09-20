"""Create a Python program using NumPy that:
Imports NumPy.
Creates a NumPy array containing at least 10 numbers.
Displays the array.
Displays the array's shape, size, and data type.
Creates a one-dimensional and two-dimensional array."""

import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("NumPy Array:")
print(numbers)

print("\nShape:", numbers.shape)
print("Size:", numbers.size)
print("Data Type:", numbers.dtype)

one_dimensional = np.array([1, 2, 3, 4, 5])

two_dimensional = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\nOne-Dimensional Array:")
print(one_dimensional)

print("\nTwo-Dimensional Array:")
print(two_dimensional)