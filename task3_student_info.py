# kamal subedi ###Q.(3) implement a program to store student records(name, roll, marks, contact number) 
# using a dictionary.  (a). provide menu to add , search , and display student.
def add_student(students):
    roll = input("Enter Roll Number: ")
    if roll in students:
        print("A student with this roll number already exists.")
        return
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    contact = input("Enter Contact Number: ")
    students[roll] = {
        'name': name,
        'marks': marks,
        'contact': contact
    }
    print("Student added successfully.\n")

def search_student(students):
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        print("\n--- Student Found ---")
        print(f"Roll No: {roll}")
        print(f"Name: {students[roll]['name']}")
        print(f"Marks: {students[roll]['marks']}")
        print(f"Contact: {students[roll]['contact']}\n")
    else:
        print("Student not found.\n")

def display_all_students(students):
    if not students:
        print("No student records to display.\n")
        return
    print("\n--- All Student Records ---")
    for roll, info in students.items():
        print(f"Roll No: {roll}")
        print(f"Name: {info['name']}")
        print(f"Marks: {info['marks']}")
        print(f"Contact: {info['contact']}")
        print("-" * 30)
    print()

def main():
    students = {}

    while True:
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            search_student(students)
        elif choice == '3':
            display_all_students(students)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the main function
main()
