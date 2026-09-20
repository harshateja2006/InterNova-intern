"""Write Python programs to:

Print numbers from 1 to 20 using a for loop.
Print the multiplication table of any number.
Print even numbers from 1 to 50 using a while loop."""

number = int(input("Enter a number: "))

print("\nFor loop")

print("\nMultiplication Table")
print("--------------------")

for i in range(1, 6):
    print(number, "x", i, "=", number * i)

print("\nwhile loop")

number = 2
while number <= 10:
    print(number,end=' ')
    number += 2