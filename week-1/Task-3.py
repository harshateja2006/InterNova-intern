"""Create a calculator program that performs:
Addition
Subtraction
Multiplication
Division
Modulus using two numbers entered by the user."""

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nCalculator Result")
print("-----------------")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
    print("Modulus:", num1 % num2)
else:
    print("Division: Cannot divide by zero")
    print("Modulus: Cannot divide by zero")