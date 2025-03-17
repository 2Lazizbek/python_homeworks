import pandas as pd

# Read the Parquet file into a DataFrame
flights_df = pd.read_parquet('flights.parquet')

# Use info() to summarize the DataFrame
print(flights_df.info())

# Extract and print only the 'origin', 'dest', and 'carrier' columns
flights_selected = flights_df[['origin', 'dest', 'carrier']]

print(flights_selected.head())

# Find the number of unique destinations
unique_destinations = flights_df['dest'].nunique()

print("\nNumber of unique destinations:", unique_destinations)

# Check for missing values in the dataset
missing_values = flights_df.isnull().sum()

print("Missing values in each column:")
print(missing_values)

# Fill missing values in the 'dep_delay' column with its mean
flights_df['dep_delay'] = flights_df['dep_delay'].fillna(flights_df['dep_delay'].mean())

# Verify that missing values are filled
print("Missing values in 'dep_delay' after filling:")
print(flights_df['dep_delay'].isnull().sum())