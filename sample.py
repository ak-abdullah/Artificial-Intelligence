import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('faculty.csv')

# Shuffle the DataFrame
shuffled_df = df.sample(frac=1).reset_index(drop=True)

# Write the shuffled DataFrame to a new CSV file
shuffled_df.to_csv('faculty.csv', index=False)

print("Data shuffled and saved to shuffled_student_data.csv")
