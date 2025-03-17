import pandas as pd
# Load the movie.csv file
df_movies = pd.read_csv('movie.csv')

# Create two smaller DataFrames
df_color = df_movies[['director_name', 'color']]
df_reviews = df_movies[['director_name', 'num_critic_for_reviews']]

# Perform a left join
df_left_join = pd.merge(df_color, df_reviews, on='director_name', how='left')

# Perform a full outer join
df_full_outer_join = pd.merge(df_color, df_reviews, on='director_name', how='outer')

# Count rows in resulting DataFrames
print(f"Left Join Rows: {len(df_left_join)}")
print(f"Full Outer Join Rows: {len(df_full_outer_join)}")