import requests
from bs4 import BeautifulSoup

# url = "http://www.datacamp.com/teach/documentation"

# # Check the reponse
# r = requests.get(url)
# print(r.status_code)

# Extracting Response
# print(r.text)

# Parsing HTML using Beautiful Soup
scrap_url = "https://www.python.org/~guido/"

r = requests.get(scrap_url)

# Check Status
if r.status_code == 200:
    print("Status:", r.status_code)
else:
    print("Bad Request:", r.status_code)

# Get Text
html_doc = r.text

# Creating Soup
soup = BeautifulSoup(html_doc, features="html.parser")
# print(soup.prettify())

# Get the Title
guido_title = soup.title
print(guido_title)

# Get the text
guido_text = soup.get_text()
print(guido_text)

# Get all Hyperlinks
a_tags = soup.find_all("a")

for link in a_tags:
    print(link.get("href"))
