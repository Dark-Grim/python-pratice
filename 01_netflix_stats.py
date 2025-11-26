# Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt


# Use netflix_data.csv to solve below TODO's
df = pd.read_csv("./Data/netflix_data.csv")
# print(df.head())


# TODO What was the most frequent movie duration in the 1990s? Save an approximate answer as an integer called duration (use 1990 as the decade's start year).

# Filter for decades and type
movie1990s = (
    (df["release_year"] >= 1990) & (df["release_year"] < 2000) & (df["type"] == "Movie")
)

# mode() -> gives the most common duration.
duration_1990s = df.loc[movie1990s, "duration"]
most_frequent_duration = duration_1990s.mode().iloc[0]
print("Most frequent movie duration in the 1990s:", most_frequent_duration)


# TODO A movie is considered short if it is less than 90 minutes. Count the number of short action movies released in the 1990s and save this integer as short_movie_count.

# Adding filters
action_movies = (
    (df["release_year"] >= 1990)
    & (df["release_year"] < 2000)
    & (df["genre"] == "Action")
    & (df["duration"] < 90)
)

# shape[0] -> gives the row count only.
print("Short action movies in the 1990s:", df[action_movies].shape[0])
