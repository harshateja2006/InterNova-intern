"""Mini Python Project

Develop a Student Record Management System using Python.

The program should:

Add student details.
Display all student records.
Search a student by name.
Delete a student record.
Use lists or dictionaries for data storage."""

students = []

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    branch = input("Enter branch: ")
    
    student = {
        "Name": name,
        "Roll No": roll_no,
        "Branch": branch
    }
    
    students.append(student)
    print("Student added successfully.")

def display_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        print("\nStudent Records")
        print("----------------")
        for student in students:
            print("Name:", student["Name"])
            print("Roll No:", student["Roll No"])
            print("Branch:", student["Branch"])
            print("----------------")

def search_student():
    name = input("Enter student name to search: ")
    found = False
    
    for student in students:
        if student["Name"].lower() == name.lower():
            print("\nStudent Found")
            print("Name:", student["Name"])
            print("Roll No:", student["Roll No"])
            print("Branch:", student["Branch"])
            found = True
            break
    
    if not found:
        print("Student not found.")

def delete_student():
    name = input("Enter student name to delete: ")
    
    for student in students:
        if student["Name"].lower() == name.lower():
            students.remove(student)
            print("Student deleted successfully.")
            return
    
    print("Student not found.")

while True:
    print("\nStudent Record Management System")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Program ended.")
        break
    else:
        print("Invalid choice.")