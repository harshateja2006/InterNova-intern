"""Basic File Handling
Write a Python program that:

Creates a text file.
Writes your introduction into the file.
Reads and displays the file contents."""

file = open("introduction.txt", "w")

file.write("My name is Harsha.\n")
file.write("I am studying at Raghu.\n")
file.write("My branch is CSD.")

file.close()

file = open("introduction.txt", "r")

content = file.read()

print("File Contents:")
print("----------------")
print(content)

file.close()