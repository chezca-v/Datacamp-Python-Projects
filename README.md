📊 EDA: Netflix Movies from the 1990s
This script performs basic exploratory data analysis (EDA) on netflix_data.csv to understand patterns in movie durations and genres during the 1990s. Specifically, it:

- Filters the dataset to include only movies released from 1990 to 1999.

- Identifies the most common movie duration (in minutes) for that decade.

- Counts how many short action movies (duration < 90 minutes) were released during this period.



It uses the pandas library to read, clean, and analyze the data, and provides two outputs:

- duration: Most frequent movie duration (as an integer)

- short_movie_count: Count of short action movies from the 1990s

### Requirements:
- Python 3
- pandas
- matplotlib
