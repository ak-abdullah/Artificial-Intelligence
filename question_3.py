from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
import pandas as pd
import random
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
def generate_pdf(filename):
    df = pd.read_csv(filename)
    if filename.endswith('students.csv'):
        df = df.drop(['Domain_Count', 'cluster'], axis=1)

    df['Room'] = pd.to_numeric(df['Room']).astype(int)

    # Create PDF
    file_name_without_extension = filename.split(".")[0]
    pdf_filename = f'{file_name_without_extension}.pdf'
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    content = []

    # Convert DataFrame to list of lists
    data = [df.columns.tolist()] + df.values.tolist()

    # Determine column widths (you can adjust these values)
    num_cols = len(df.columns)
    col_widths = [100] * num_cols  # Example: setting each column width to 100

    # Create Table object with specified column widths
    pdf_table = Table(data, colWidths=col_widths)

    # Style the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header background color
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # All cells centered
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Row background color
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Grid lines
    ])
    pdf_table.setStyle(style)
    content.append(pdf_table)
    doc.build(content)
    print(f"PDF saved as {pdf_filename}")


def delete_files():
    directory_path = "C:/Users/HP/Desktop/AI Lab/Project"

# Specify the names of the files you want to keep
    files_to_keep = ["faculty.csv", "student_data.csv"]

    # List all files in the directory
    all_files = os.listdir(directory_path)

    # Iterate over the files and delete the CSV files except the ones you want to keep
    for file_name in all_files:
        if file_name.endswith(".csv") and file_name not in files_to_keep:
            file_path = os.path.join(directory_path, file_name)
            os.remove(file_path)

delete_files()
df = pd.read_csv("student_data.csv")
domain_counts = df['Batch'].value_counts()
department_counts_dict = {}

for domain, count in domain_counts.items():
    department_counts_dict[domain] =  int(count)
    print(int(count))

df['Domain_Count'] = df['Domain'].map(department_counts_dict)

features = ['Domain_Count', 'Batch']

km = KMeans(n_clusters=5)



y_predicted = km.fit_predict(df[features])
centroids = km.cluster_centers_
df['cluster'] = y_predicted


for i in range(5): 
    cluster_i = df[df['cluster'] == i]
    cluster_i.to_csv(f"cluster_{i}.csv", index=False)
    department_value = cluster_i.iloc[0]['Domain']

Majority_Rooms_value = random.randint(25, 28)

Rooms = []
for i in range(Majority_Rooms_value + (30 - Majority_Rooms_value)):
    if i < Majority_Rooms_value:
        Rooms.append(random.randint(30, 35))
    else:
        Rooms.append(25)
random.shuffle(Rooms)
cpy_rooms = Rooms.copy() 
k = 0
room_a = 1
fc = pd.read_csv("faculty.csv")
ra = pd.DataFrame(columns=['First Name', 'Last Name', 'Department', 'Room'])
Faculty = ['Software Engineering', 'Computer Science', 'Business Analytics', 'Artificial Intelligence', 'Electrical Engineering']
for i in range(5):
    df = pd.read_csv(f"cluster_{i}.csv")
    department_value = df.iloc[0]['Domain']
    department_faculty = fc[fc['Department'] == department_value]    
    for index, student in df.iterrows():
        if Rooms[k] == 0:
            
            row_department_faculty = department_faculty.iloc[room_number - 1]
            
            first_name = row_department_faculty['First Name']
            last_name = row_department_faculty['Last Name']
            department = row_department_faculty['Department']
            ra.at[room_number - 1, 'Room'] = room_number
            ra.at[room_number - 1, 'First Name'] = first_name
            ra.at[room_number - 1, 'Last Name'] = last_name
            ra.at[room_number - 1, 'Department'] = department
            if k == 30 - 1:
                # print("Rooms are Full Now Rooms will be generated for another time with start Room 1")
                ra.to_csv(f"Rooms_Assignment {room_a}.csv", index=False)
                ra = pd.DataFrame(columns=['First Name', 'Last Name', 'Department', 'Room'])
                room_a += 1
                
                Rooms = cpy_rooms.copy()
                k = -1
            k += 1
        elif index == len(df) - 1:
            row_department_faculty = department_faculty.iloc[room_number - 1]
            
            first_name = row_department_faculty['First Name']
            last_name = row_department_faculty['Last Name']
            department = row_department_faculty['Department']
            ra.at[room_number - 1, 'Room'] = room_number
            ra.at[room_number - 1, 'First Name'] = first_name
            ra.at[room_number - 1, 'Last Name'] = last_name
            ra.at[room_number - 1, 'Department'] = department
            if i == 5 - 1:
                ra.to_csv(f"Rooms_Assignment {room_a}.csv", index=False)
        
            
        room_number = k + 1
        Rooms[k] = Rooms[k] - 1
        df.at[index, 'Room'] = room_number
    df.to_csv(f"cluster_{i}.csv", index=False)

file1 = pd.read_csv("cluster_0.csv")
file2 = pd.read_csv("cluster_1.csv")
file3 = pd.read_csv("cluster_2.csv")
file4 = pd.read_csv("cluster_3.csv")
file5 = pd.read_csv("cluster_4.csv")


# Concatenate all DataFrames into a single DataFrame
merged_df = pd.concat([file1, file2, file3, file4, file5], ignore_index=True)

merged_df.to_csv("merged_data.csv", index=False)
merged_df = pd.read_csv("merged_data.csv")
    
a = 0
start_index = 0
l = []
for index, student in merged_df.iterrows():
    if merged_df.iloc[index]["Room"] == 1 and index > 0 and merged_df.iloc[index - 1]["Room"] > 1:
        split_df = merged_df.iloc[start_index:index]
        string = input("Enter Time For Seating Plan: ")
        l.append(string)
        split_df.to_csv(f"{string}_students.csv", index=False)
        start_index = index
        a += 1
    elif index == len(merged_df) - 1:
        split_df = merged_df.iloc[start_index:index + 1]
        string = input("Enter Time For Seating Plan: ")
        split_df.to_csv(f"{string}_students.csv", index=False)
        l.append(string)
for i in range(5):
    os.remove(f"cluster_{i}.csv")

for i in range(a + 1):
    current_name = f"Rooms_Assignment {i + 1}.csv"
    new_name = f"{l[i]}_faculty.csv"
    if not os.path.exists(new_name):
        os.rename(current_name, new_name)


for i in range(a + 1):
    file_name = f'{l[i]}_students.csv'
    df = pd.read_csv(file_name)
    df[['year_prefix', 'numeric_part']] = df['Roll Number'].str.split('-', expand=True)
    df['numeric_part'] = df['numeric_part'].astype(int)
    df_sorted = df.sort_values(by=['year_prefix', 'numeric_part'])
    df_sorted.drop(columns=['year_prefix', 'numeric_part'], inplace=True)
    df_sorted.to_csv(file_name, index=False)

for i in range(a + 1):
    file1 = f"{l[i]}_faculty.csv"
    file2 = f"{l[i]}_students.csv"
    generate_pdf(file1)
    generate_pdf(file2)

# delete_files()
