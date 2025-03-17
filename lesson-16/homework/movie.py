import pandas as pd

# Load the CSV file into a DataFrame
movie_df = pd.read_csv('movie.csv')

# Display a random sample of 10 rows
print(movie_df.sample(10))

# Filter rows where duration is greater than 120 minutes
movies_filtered = movie_df[movie_df['duration'] > 120]

# Sort the filtered DataFrame by 'director_facebook_likes' in descending order
movies_sorted = movies_filtered.sort_values('director_facebook_likes', ascending=False)

print(movies_sorted.head())

# Group by director and sum their Facebook likes
director_likes = movie_df.groupby('director_name')['director_facebook_likes'].sum()

# Find the director with the highest total likes
top_director = director_likes.idxmax()
top_likes = director_likes.max()

print(f"Director with the highest total Facebook likes: {top_director} ({top_likes} likes)")