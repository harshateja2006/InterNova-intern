""" Strings & Collections

Create programs to demonstrate:

String operations (upper(), lower(), replace(), find())
List operations (append(), remove(), sort())
Tuple creation and indexing
Dictionary storing student information
Set operations (add(), remove())"""

text = "python programming"

print("Original String:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Replace:", text.replace("python", "data"))
print("Position of programming:", text.find("programming"))

numbers = [30, 10, 20]
print("\nOriginal List:", numbers)

numbers.append(40)
print("After Append:", numbers)

numbers.remove(10)
print("After Remove:", numbers)

numbers.sort()
print("After Sort:", numbers)

student = ("Harsha", "CSD", 21)
print("\nTuple:", student)
print("First Element:", student[0])
print("Second Element:", student[1])

student_info = {
    "Name": "Harsha",
    "College": "Raghu",
    "Branch": "CSD"
}

print("\nStudent Dictionary:", student_info)
print("Student Name:", student_info["Name"])
print("College:", student_info["College"])
print("Branch:", student_info["Branch"])

subjects = {"Python", "SQL", "Excel"}
print("\nOriginal Set:", subjects)

subjects.add("Power BI")
print("After Add:", subjects)

subjects.remove("Excel")
print("After Remove:", subjects)