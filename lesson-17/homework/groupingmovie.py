import pandas as pd
# Load the movie.csv file
df_movies = pd.read_csv('movie.csv')

# Group by color and director_name
df_movie_grouped = df_movies.groupby(['color', 'director_name']).agg(
    TotalReviews=('num_critic_for_reviews', 'sum'),
    AverageDuration=('duration', 'mean')
).reset_index()

print(df_movie_grouped.head())