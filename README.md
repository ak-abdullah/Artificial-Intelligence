# AI-Based Student Clustering and Examination Report Generator

## 📌 Project Overview

This project utilizes **K-Means Clustering**, an unsupervised machine learning algorithm, to group students based on their **domain of study** and **batch year**. The primary objective is to automate the clustering process for examination purposes and generate personalized **PDF reports** for both **students** and **faculty**.

The project is based on real data from **FAST-NUCES**, using both student and faculty datasets.

---

## 🎯 Key Features

- 📊 Cluster students based on domain and batch using K-Means
- 🧠 Apply unsupervised machine learning for intelligent grouping
- 📁 Preprocess and handle real student/faculty datasets from FAST-NUCES
- 📄 Generate PDF reports:
  - Individual student report with cluster info
  - Faculty-wise student cluster reports
- 🧾 Assist faculty in examination preparation and student evaluation

---

## 📂 Dataset Description

Two datasets were used:

- **Student Dataset**:
  - Name
  - Roll Number
  - Batch
  - Domain (AI, Web, Data Science, etc.)

- **Faculty Dataset**:
  - Name
  - Domain
  - Assigned students (optional)

> Note: All datasets are anonymized and used solely for academic purposes.

---

## 🧪 Technologies Used

- Python
  - `scikit-learn` for K-Means clustering
  - `pandas` for data handling
  - `fpdf` or `reportlab` for PDF report generation
- Jupyter Notebook or Python Script

---

## 🚀 How It Works

1. **Load Data**: Read and clean student and faculty data from CSV files.
2. **Cluster Students**: Use K-Means on features like domain and batch to group students.
3. **Map Faculty**: Optionally match faculty to clusters by domain.
4. **Generate Reports**: Export student and faculty reports as PDFs.

---

## 📎 Output

- `student_report_<roll_number>.pdf`
- `faculty_report_<faculty_name>.pdf`

Each report includes:
- Cluster ID
- Student/peer list
- Batch and domain info
- Assigned faculty (if applicable)

---

## 📈 Use Cases

- Viva or Capstone Project evaluation grouping
- Faculty planning for student assessments
- Automated student group assignment
