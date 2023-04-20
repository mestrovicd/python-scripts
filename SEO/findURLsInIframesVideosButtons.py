import sys
import requests
from bs4 import BeautifulSoup
import winsound

# Check if the correct number of command line arguments were provided
if len(sys.argv) != 3:
    print("Usage: python findURLsInIframesVideosButtons.py [input_file] [output_file]")
    sys.exit()

# Notify the user that this process can take some time, depending on the amount of input URLs
print(
    "This process might take up to a couple of minutes, depending on the amount of input URLs"
)

# Get the input file and output file names from the command line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Read the list of URLs from the input file
with open(input_file, "r") as file:
    urls = file.read().splitlines()

# Create an empty list to store all the iframe, video, and button components
components = []

# Loop through each URL and extract its iframe, video, and button components
for url in urls:
    # Send a GET request to the URL and get the page's HTML content
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all the <iframe> and <video> tags on the page
    iframes = soup.find_all("iframe")
    videos = soup.find_all("video")

    # Add the iframe and video components to the list
    for iframe in iframes:
        components.append(iframe["src"])
    for video in videos:
        components.append(video["src"])

    # Find all the <button> tags on the page with a data-v-src attribute
    buttons = soup.find_all("button", {"data-v-src": True})

    # Add the button components to the list
    for button in buttons:
        components.append(button["data-v-src"])

# Write the components to the output file
with open(output_file, "w") as file:
    for component in components:
        file.write(component + "\n")

# beep at the end of the program to notify user it's over
winsound.Beep(500, 1000)
