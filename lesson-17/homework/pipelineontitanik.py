import pandas as pd

# Load Titanic dataset
df_titanic = pd.read_excel('titanic.xlsx')

# Define pipeline functions
def filter_survived(df):
    return df[df['Survived'] == 1]

def fill_missing_age(df):
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    return df

def add_fare_per_age(df):
    df['Fare_Per_Age'] = df['Fare'] / df['Age']
    return df

# Apply pipeline
df_titanic_pipeline = (df_titanic
                       .pipe(filter_survived)
                       .pipe(fill_missing_age)
                       .pipe(add_fare_per_age))

print(df_titanic_pipeline.head())