import pandas as pd

# Load movies dataset
df_movies = pd.read_csv('movie.csv')

# Function to classify movie duration
def classify_duration(duration):
    if duration < 60:
        return 'Short'
    elif 60 <= duration <= 120:
        return 'Medium'
    else:
        return 'Long'

# Apply the function to classify movies
df_movies['Duration_Class'] = df_movies['duration'].apply(classify_duration)

print(df_movies[['duration', 'Duration_Class']].head())