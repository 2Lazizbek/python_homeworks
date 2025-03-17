import pandas as pd
# Load flights dataset
df_flights = pd.read_parquet('\flights')

# Group by Year and Month
df_flights_grouped = df_flights.groupby(['Year', 'Month']).agg(
    TotalFlights=('FlightNumber', 'count'),
    AverageArrDelay=('ArrDelay', 'mean'),
    MaxDepDelay=('DepDelay', 'max')
).reset_index()

print(df_flights_grouped.head())