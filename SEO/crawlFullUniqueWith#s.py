# crawls the website, outputs all unique URLs under domain to txt
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import winsound

# Check if the correct number of command line arguments were provided
if len(sys.argv) != 3:
    print("Usage: python crawlFullUniqueWith#s.py [url] [output_file]")
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
        # If the URL is relative, join it with the base URL to create an absolute URL
        abs_url = urljoin(url, href)
        if abs_url.startswith(url):
            urls.append(abs_url)

# Remove duplicates from the list
urls = list(set(urls))

# Write the URLs to the output file
with open(output_file, "w") as file:
    for url in urls:
        # If the URL starts with the base URL, write it with a relative path
        if url.startswith(url):
            file.write(url[len(url) - len(url) :] + "\n")
        # Otherwise, write it with an absolute path
        else:
            file.write(url + "\n")

print("Total number of URLs crawled:", len(urls))

winsound.Beep(250, 400)
winsound.Beep(250, 400)
