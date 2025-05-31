# Q(6). develop a simple OOP-based python class student with attributes 
# like name, roll number, and marks . implement methods to input display details.
class Student:
    def __init__(self):
        self.name = ""
        self.roll_number = ""
        self.marks = 0

    def input_details(self):
        self.name = input("Enter student's name: ")
        self.roll_number = input("Enter roll number: ")
        self.marks = float(input("Enter marks: "))

    def display_details(self):
        print("\n--- Student Details ---")
        print(f"Name       : {self.name}")
        print(f"Roll No.   : {self.roll_number}")
        print(f"Marks      : {self.marks}")


# Example usage
student1 = Student()
student1.input_details()
student1.display_details()
