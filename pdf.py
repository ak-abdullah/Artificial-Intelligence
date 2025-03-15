
def generate_pdf(filename):
    df = pd.read_csv(filename)
    df = df.drop(['Domain_Count', 'cluster'], axis=1)

    df['Room'] = pd.to_numeric(df['Room']).astype(int)

    # Create PDF
    pdf_filename = 'students_report.pdf'
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
