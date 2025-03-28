import pandas as pd
# Load Titanic dataset
df_titanic = pd.read_excel('titanic.xlsx')

# Group by Pclass and calculate aggregations
df_grouped = df_titanic.groupby('Pclass').agg(
    AverageAge=('Age', 'mean'),
    TotalFare=('Fare', 'sum'),
    PassengerCount=('PassengerId', 'count')
).reset_index()

# Save to a new DataFrame
df_grouped.to_csv('titanic_grouped.csv', index=False)
print(df_grouped)