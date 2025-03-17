import pandas as pd

# Load the Excel file into a DataFrame
titanic_df = pd.read_excel('titanic.xlsx')

# Display the first 5 rows
print(titanic_df.head())

# Filter rows where the age of passengers is above 30
titanic_filtered = titanic_df[titanic_df['Age'] > 30]

# Count the number of male and female passengers
gender_counts = titanic_df['Sex'].value_counts()

print("Passengers above 30 years old:")
print(titanic_filtered.head())

print("\nNumber of male and female passengers:")
print(gender_counts)

# Calculate min, max, and sum of passenger ages
age_stats = titanic_df['Age'].agg(['min', 'max', 'sum'])

print(age_stats)