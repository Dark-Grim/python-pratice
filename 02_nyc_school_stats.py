import pandas as pd

# Read in the data
schools = pd.read_csv("./Data/schools.csv")

# Preview the Data
# print(school.head())

# TODO
# Which NYC schools have the best math results?

# The best math results are at least 80% of the *maximum possible score of 800* for math.
# Save your results in a pandas DataFrame called best_math_schools, including "school_name" and "average_math" columns, sorted by "average_math" in descending order.

# Steps Followed:

# max_possible_score = school["average_math"].max()
# best_math_result = school["average_math"] / max_possible_score
# filter = best_math_result * 100

# SOLUTION: 1

schools["best_math_percent"] = (schools["average_math"] / 800) * 100

best_math_schools = schools[schools["best_math_percent"] > 80][
    ["school_name", "average_math"]
].sort_values("average_math", ascending=False)

# print(best_math_schools)


# TODO
# What are the top 10 performing schools based on the combined SAT scores?

# Save your results as a pandas DataFrame called top_10_schools containing the "school_name" and a new column named "total_SAT", with results ordered by "total_SAT" in descending order ("total_SAT" being the sum of math, reading, and writing scores).

# SOLUTION: 2

schools["total_SAT"] = (
    schools["average_math"] + schools["average_reading"] + schools["average_writing"]
)

top_10_schools = (
    schools[["school_name", "total_SAT"]]
    .sort_values("total_SAT", ascending=False)
    .head(10)
)

# print(top_10_schools)


# TODO
# Which single borough has the largest standard deviation in the combined SAT score?

# Save your results as a pandas DataFrame called largest_std_dev.
# The DataFrame should contain one row, with:
# "borough" - the name of the NYC borough with the largest standard deviation of "total_SAT".
# "num_schools" - the number of schools in the borough.
# "average_SAT" - the mean of "total_SAT".
# "std_SAT" - the standard deviation of "total_SAT".
# Round all numeric values to two decimal places.

# SOLUTION: 3

bourogh_stats = schools.groupby("borough").agg(
    total_SAT=("total_SAT", "sum"),
    num_schools=("school_name", "count"),
    average_SAT=("total_SAT", "mean"),
    std_SAT=("total_SAT", "std"),
)

bourogh_stats = bourogh_stats.round(2)

largest_std_dev = bourogh_stats.sort_values("std_SAT", ascending=False)
# largest_std_dev = bourogh_stats.loc[bourogh_stats["std_SAT"].idxmax()]

largest_std_dev = largest_std_dev.head(1)
print(largest_std_dev)
