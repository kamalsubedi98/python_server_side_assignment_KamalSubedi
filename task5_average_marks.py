# Q(5). write python code to read  from a CSV file of 
# student marks and calculate average marks.

import csv
import os

def create_sample_csv(filename):
    sample_data = [
        {"name": "Kamal", "marks": 85},
        {"name": "Sita", "marks": 90},
        {"name": "Hari", "marks": 78},
        {"name": "Gita", "marks": 92},
        {"name": "Ramesh", "marks": 88}
    ]

    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "marks"])
        writer.writeheader()
        writer.writerows(sample_data)
    print(f"'{filename}' created with sample data.\n")

def calculate_average_marks(filename):
    total_marks = 0
    count = 0

    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    marks = float(row['marks'])
                    total_marks += marks
                    count += 1
                except ValueError:
                    print(f"Invalid marks for student '{row['name']}' — skipping.")

        if count > 0:
            average = total_marks / count
            print(f"Average Marks of {count} students: {average:.2f}")
        else:
            print("No valid marks found.")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except KeyError:
        print("CSV file must contain a 'marks' column.")

def main():
    filename = "marks.csv"
    if not os.path.exists(filename):
        create_sample_csv(filename)

    calculate_average_marks(filename)

if __name__ == "__main__":
    main()
