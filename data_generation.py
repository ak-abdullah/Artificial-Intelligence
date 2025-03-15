import csv
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Define batch numbers and domains of study
batches = ['19', '20', '21', '22', '23']
domains = ['Computer Science', 'Artificial Intelligence', 'Business Analytics', 'Software Engineering', 'Electrical Engineering']

# Generate synthetic student data
def generate_student_data(num_students):
    students = []
    for _ in range(num_students):
        batch = random.choice(batches)
        domain = random.choice(domains)
        roll_number = f"{batch}F-{random.randint(1000, 9999)}"
        first_name = fake.first_name()
        last_name = fake.last_name()
        students.append({'Roll Number': roll_number, 'First Name': first_name, 'Last Name': last_name, 'Batch': batch, 'Domain': domain})
    return students

# Example: Generate 1000 students
num_students = 1000
student_data = generate_student_data(num_students)

# Save student data to CSV file
csv_file = "student_data.csv"
fieldnames = ['Roll Number', 'First Name', 'Last Name', 'Batch', 'Domain']

with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for student in student_data:
        writer.writerow(student)

print(f"Student data has been saved to {csv_file}.")
