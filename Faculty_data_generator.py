import csv
import random
from faker import Faker

departments = ["Computer Science", "Electrical Engineering", "Software Engineering", "Business Analytics", "Artificial Intelligence"]
fake = Faker()

def generate_faculty(department, count):
    faculty_list = []
    for i in range(count):
        first_name = fake.first_name()
        last_name = fake.last_name()
        faculty_list.append({
            "First Name": first_name,
            "Last Name": last_name,
            "Department": department,
            "Age": random.randint(25, 65),
            "Gender": random.choice(["Male", "Female"])
        })
    return faculty_list

# Generating faculty for each department
all_faculty = []
for department in departments:
    department_faculty = generate_faculty(department, 30)
    all_faculty.extend(department_faculty)

# Writing faculty data to CSV
csv_columns = ["First Name", "Last Name", "Department", "Age", "Gender"]
csv_file = "faculty.csv"

try:
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for faculty in all_faculty:
            writer.writerow(faculty)
    print("CSV file has been created successfully!")
except IOError:
    print("I/O error")
