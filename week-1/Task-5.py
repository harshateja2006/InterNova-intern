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