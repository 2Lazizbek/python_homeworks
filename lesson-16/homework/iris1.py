import pandas as pd

# Load the JSON file into a DataFrame
iris_df = pd.read_json('iris.json')

# Show the shape of the dataset
print("Shape of the dataset:", iris_df.shape)

# Show the column names
print("Column names:", iris_df.columns)

# Rename the columns to lowercase
iris_df.columns = iris_df.columns.str.lower()

# Select only the 'sepal_length' and 'sepal_width' columns
iris_selected = iris_df[['sepallength', 'sepalwidth']]

print(iris_selected.head())
print()
# Calculate mean, median, and standard deviation for each numerical column
iris_stats = iris_df[['sepallength', "sepalwidth", "petallength", "petalwidth"]].agg(['mean', 'median', 'std'])

print(iris_stats)