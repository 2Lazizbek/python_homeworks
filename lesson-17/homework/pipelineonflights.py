import pandas as pd
# Load flights dataset
df_flights = pd.read_parquet('\flights')

# Define pipeline functions
def filter_delayed_flights(df):
    return df[df['DepDelay'] > 30]

def add_delay_per_hour(df):
    df['Delay_Per_Hour'] = df['DepDelay'] / df['FlightDuration']
    return df

# Apply pipeline
df_flights_pipeline = (df_flights
                       .pipe(filter_delayed_flights)
                       .pipe(add_delay_per_hour))

print(df_flights_pipeline.head())