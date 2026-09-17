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