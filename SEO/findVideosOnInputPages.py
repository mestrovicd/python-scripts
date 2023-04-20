import sys
import requests
from bs4 import BeautifulSoup
import winsound

# Check input args
if len(sys.argv) != 3:
    print("Usage: python findVideosOnInputPages.py [input_file] [output_file]")
    sys.exit()

print(
    "This process takes a couple of minutes, depending on the amount of input URLs and videos on them..."
)

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r") as file:
    urls = file.read().splitlines()

video_url_appearances = {}

for url in urls:
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")

    # Find all the <iframe>, <video> and <button data-v-src=""> tags on the page
    iframes = soup.find_all("iframe")
    videos = soup.find_all("video")
    buttons = soup.find_all("button", {"data-v-src": True})

    # Add the iframe, video and button components to the dictionary
    for component in iframes + videos:
        src = component["src"]

        # Exclude GTM URLs
        if not src.startswith("https://www.googletagmanager.com"):
            if src in video_url_appearances:
                video_url_appearances[src].append(url)
            else:
                video_url_appearances[src] = [url]

    for button in buttons:
        src = button["data-v-src"]
        if not src.startswith("https://www.googletagmanager.com"):
            if src in video_url_appearances:
                video_url_appearances[src].append(url)
            else:
                video_url_appearances[src] = [url]

# Output to file
with open(output_file, "w") as file:
    for video_url, appearances in video_url_appearances.items():
        file.write(video_url + ",")
        appearances = list(set(appearances))  # remove duplicates
        file.write(",".join(appearances))
        file.write("\n")

# Program exit
print("\nDone, results in: " + output_file)
print(
    "Found "
    + str(len(video_url_appearances.items()))
    + " videos on "
    + str(len(urls))
    + " pages"
)
# Beep beep
winsound.Beep(250, 400)
winsound.Beep(250, 400)
