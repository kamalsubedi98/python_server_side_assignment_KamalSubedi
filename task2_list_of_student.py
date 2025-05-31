# Q (2) create a program that takes a list of student names and stores
# them in a file , Then ,read the file and display the contents.
def write_student_names(filename):
    num = int(input("How many student names do you want to enter? "))
    with open(filename, 'w') as file:
        for i in range(num):
            name = input(f"Enter name of student {i+1}: ")
            file.write(name + '\n')
    print(f"\n{num} student names have been written to '{filename}'.")

def read_and_display_names(filename):
    print(f"\nReading contents from '{filename}':")
    try:
        with open(filename, 'r') as file:
            content = file.readlines()
            if content:
                for line in content:
                    print(line.strip())
            else:
                print("The file is empty.")
    except FileNotFoundError:
        print("The file does not exist.")

# Use the specified file name
filename = "student_details.txt"

# Write and read operations
write_student_names(filename)
read_and_display_names(filename)
