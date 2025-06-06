import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Filter for movies only
movies_df = df[df['type'] == 'Movie']

# Filter movies released between 1990 and 1999
movies_90s = movies_df[(movies_df['release_year'] >= 1990) & (movies_df['release_year'] <= 1999)]

# Ensure the "duration" column is of string type
movies_90s['duration'] = movies_90s['duration'].astype(str)

# Extract numeric duration from "duration" column (e.g., "95 min" → 95)
movies_90s['duration_mins'] = movies_90s['duration'].str.extract('(\d+)').astype(float)

# Find the most frequent (mode) duration
duration = int(movies_90s['duration_mins'].mode()[0])

# Filter short movies (< 90 minutes)
short_movies = movies_90s[movies_90s['duration_mins'] < 90]

# Filter for "Action" in genre column (case insensitive)
short_action_movies = short_movies[short_movies['genre'].str.contains('Action', case=False, na=False)]

# Count short action movies
short_movie_count = short_action_movies.shape[0]

# Final outputs
print("Most frequent movie duration in the 1990s:", duration)
print("Number of short action movies in the 1990s:", short_movie_count)
