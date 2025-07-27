import pandas as pd
df = pd.read_csv("final_college_student_placement_dataset.csv")

#Categorize placed students into salary bands
def categorize_salary(sal):
    if pd.isnull(sal):
        return None
    elif sal < 300000:
        return "Low"
    elif sal <= 600000:
        return "Medium"
    else:
        return "High"

df['Salary_Band'] = df['Salary'].apply(categorize_salary)
print("\nTask 1: Salary Band Distribution")
print(df['Salary_Band'].value_counts(dropna=False))

#Placement rate, avg salary, avg MBA score by gender & specialization
group_stats = df.groupby(['Gender', 'Specialization']).agg({
    'Placement': lambda x: (x == 'Placed').mean(),
    'Salary': lambda x: x[x.notnull()].mean(),
    'MBA_Percentage': 'mean'
}).reset_index().rename(columns={
    'Placement': 'Placement_Rate',
    'Salary': 'Avg_Placed_Salary',
    'MBA_Percentage': 'Avg_MBA_Score'
})
print("\nTask 2: Gender & Specialization Stats")
print(group_stats)

#Rows with missing values
missing_row_count = df.isnull().any(axis=1).sum()
print("\nTask 3: Rows with missing values:", missing_row_count)

#Rows with missing salary
salary_missing_rows = df[df['Salary'].isnull()]
print("\nTask 4: Rows with missing Salary")
print("Zero salaries count:", (df['Salary'] == 0).sum())
print("Blank string salaries count:", (df['Salary'].astype(str).str.strip() == '').sum())

#Students with complete records
complete_records = df.dropna()
print("\nTask 5: Complete Records Count:", complete_records.shape[0])

#Duplicate entries
duplicate_rows = df[df.duplicated()]
print("\nTask 6: Duplicate Rows")
print(duplicate_rows)

#Drop all duplicates, keep first
df_nodup_all = df.drop_duplicates(keep='first')
print("\nTask 7: Dataset shape after dropping all duplicates:", df_nodup_all.shape)

#Duplicate College_IDs
duplicates_by_id = df[df.duplicated(subset='College_ID')]
print("\nTask 8: Duplicate Entries by College_ID")
print(duplicates_by_id)

#Unique Specializations
unique_specializations = df['Specialization'].dropna().unique()
print("\nTask 9: Unique Specializations")
print(unique_specializations)

#Count of unique MBA scores
unique_mba_scores = df['MBA_Percentage'].dropna().nunique()
print("\nTask 10: Unique MBA Score Count:", unique_mba_scores)

#Unique gender-specialization-status combos
unique_combos = df[['Gender', 'Specialization', 'Placement']].drop_duplicates().shape[0]
print("\nTask 11: Unique Gender-Specialization-Placement Combinations:", unique_combos)

#Average salary of placed students
avg_salary_placed = df[df['Placement'] == 'Placed']['Salary'].dropna().mean()
print("\nTask 12: Average Salary of Placed Students:", avg_salary_placed)

#Min and max CGPA
min_degree = df['CGPA'].min()
max_degree = df['CGPA'].max()
print("\nTask 13: Min CGPA:", min_degree, "| Max CGPA:", max_degree)

#Placement counts
placement_counts = df['Placement'].value_counts()
print("\nTask 14: Placement Counts")
print(placement_counts)

#Stats by Specialization
specialization_stats = df.groupby('Specialization').agg({
    'SSC_Percentage': 'mean',
    'MBA_Percentage': 'mean',
    'Placement': lambda x: (x == 'Placed').sum()
}).reset_index().rename(columns={
    'SSC_Percentage': 'Avg_SSC',
    'MBA_Percentage': 'Avg_MBA',
    'Placement': 'Placed_Count'
})
print("\nTask 15: Specialization-wise Statistics")
print(specialization_stats)

#Summary table
summary_table = pd.DataFrame({
    'Column': df.columns,
    'Null_Count': df.isnull().sum().values,
    'Unique_Values': df.nunique().values,
    'Duplicated_Value_Count': [df[df.duplicated(subset=[col])].shape[0] if col != 'Salary' else None for col in df.columns]
})
print("\nTask 16: Column Summary Table")
print(summary_table)