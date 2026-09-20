"""Using a NumPy array:
Access specific elements using indexing.
Extract a portion of the array using slicing.
Create a two-dimensional array.
Access specific rows and columns.
Reshape an array into different dimensions.
Display the original and reshaped arrays."""

import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80])

print("Original Array:")
print(numbers)

print("\nSpecific Elements:")
print("First Element:", numbers[0])
print("Fourth Element:", numbers[3])
print("Last Element:", numbers[-1])

print("\nSliced Array:")
print(numbers[2:6])

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\nTwo-Dimensional Array:")
print(matrix)

print("\nSpecific Row:")
print(matrix[1])

print("\nSpecific Column:")
print(matrix[:, 1])

print("\nSpecific Element:")
print(matrix[2, 0])

reshaped = numbers.reshape(2, 4)

print("\nReshaped Array:")
print(reshaped)