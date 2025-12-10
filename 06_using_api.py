import json
import requests

# with open("./Data/products.json", "r") as json_file:
#     json_data = json.load(json_file)

# print(type(json_data))
# print(json_data)

# for k in json_data.keys():
#     print("Keys:", k)


url = "http://www.omdbapi.com/?apikey=35bba556&t=hackers"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

for k in data.keys():
    print(k + ":", data[k])
