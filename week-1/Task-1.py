"""Create a Python program that:
Prints a welcome message.
Takes your Name, College Name, and Branch as input.
Displays the entered information in a formatted output."""

print("Welcome to Python Fundamentals for Data Analytics")

name = input("Enter your Name: ")
college = input("Enter your College Name: ")
branch = input("Enter your Branch: ")

print("\nStudent Information")
print("-------------------")
print(f"Name     : {name}")
print(f"College  : {college}")
print(f"Branch   : {branch}")