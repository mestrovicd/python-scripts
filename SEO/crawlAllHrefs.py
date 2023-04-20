# crawls the given domain for all href attributes
import sys
import requests
from bs4 import BeautifulSoup
import winsound


# Check if the correct number of command line arguments were provided
if len(sys.argv) != 3:
    print("Usage: python crawlAllHrefs.py [url] [output_file]")
    sys.exit()

# Get the URL and output file name from the command line arguments
url = sys.argv[1]
output_file = sys.argv[2]

# Send a GET request to the URL and get the page's HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all the <a> tags on the page
links = soup.find_all("a")

# Create an empty list to store all the URLs
urls = []

# Loop through each <a> tag and extract its href attribute
for link in links:
    href = link.get("href")
    if href is not None:
        urls.append(href)

# Write the URLs to the output file
with open(output_file, "w") as file:
    for url in urls:
        file.write(url + "\n")

winsound.Beep(250, 400)
winsound.Beep(250, 400)
