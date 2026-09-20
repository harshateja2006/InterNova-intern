"""Create two user-defined functions:

Function to calculate the square of a number.
Function to calculate the average of three numbers.

Call both functions with user input."""

def square(number):
    return number * number

def average(a, b, c):
    return (a + b + c) / 3

number = float(input("Enter a number to find its square: "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

print("\nSquare:", square(number))
print("Average:", average(a, b, c))