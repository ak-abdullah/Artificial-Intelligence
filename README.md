# 🤖 AI-Based Student Clustering and Examination Report Generator

## 📌 Project Overview

This project utilizes **K-Means Clustering**, an unsupervised machine learning algorithm, to group students based on their **domain of study** and **batch year**. The primary objective is to automate the clustering process for examination purposes and generate personalized **PDF reports** for both **students** and **faculty**.


---

## 🎯 Key Features

- 📊 Cluster students based on domain and batch using K-Means
- 🧠 Apply unsupervised machine learning for intelligent grouping
- 📁 Preprocess and handle student/faculty datasets
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
4. **Generate Reports**: Export student and faculty reports as PDF.

---


