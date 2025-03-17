import pandas as pd
# Load Titanic dataset
df_titanic = pd.read_csv('titanic.csv')

# Function to classify passengers
def classify_age(age):
    if age < 18:
        return 'Child'
    else:
        return 'Adult'

# Apply the function to create a new column
df_titanic['Age_Group'] = df_titanic['Age'].apply(classify_age)

print(df_titanic[['Age', 'Age_Group']].head())