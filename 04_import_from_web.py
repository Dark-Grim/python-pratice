from urllib.request import urlretrieve, urlopen, Request
import matplotlib.pyplot as plt
import pandas as pd

# Accessing URL
# url = "https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv"

# # Saving File locally
# urlretrieve(url, "./Data/winequality-red.csv")

# Reading using Pandas
df = pd.read_csv("./Data/winequality-red.csv", sep=";")
# print(df.head())

# Histogram Plot
df.iloc[:, 0].hist()
plt.xlabel("fixed acidity (g(tartaric acid)/dm$^3$)")
plt.ylabel("count")
plt.show()


# GET HTTP Request
get_url = "https://campus.datacamp.com/courses/1606/4135?ex=2"

# Send Request
request = Request(get_url)

# Catch Response
response = urlopen(request)
# print(type(response))

# Extracting Response
text = response.read()
# print(text)

# Close the Resposne
response.close()
