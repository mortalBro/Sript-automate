import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://www.geeksforgeeks.org/java-program-to-write-an-array-of-strings-to-the-output-console/"
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Extract data from specific HTML elements using CSS selectors
title = soup.select_one("h1").text
paragraphs = soup.select("p")

# Print the extracted data
print("Title:", title)
print("Paragraphs:")
for p in paragraphs:
    print(p.text)
