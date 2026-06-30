import pandas as pd

file_path = "data/raw/Data-Analytics-Full-course-Part-2-Dataset.xlsx"

df = pd.read_excel(file_path)

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nFirst 5 rows:")
print(df.head())