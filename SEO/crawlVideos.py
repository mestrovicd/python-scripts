import sys
import requests
from bs4 import BeautifulSoup
import winsound

if len(sys.argv) != 3:
    print("Usage: python findVideosOnInputPages.py [input_file] [output_file]")
    sys.exit()

input_file, output_file = sys.argv[1], sys.argv[2]

print(
    "This process takes a couple of minutes, depending on the amount of input URLs..."
)

with open(input_file) as file:
    urls = file.read().splitlines()

video_url_appearances = {}

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    components = soup.find_all(["iframe", "video"]) + soup.find_all(
        "button", {"data-v-src": True}
    )

    for component in components:
        src = component.get("src") or component.get("data-v-src")
        if not src or src.startswith("https://www.googletagmanager.com"):
            continue

        if src in video_url_appearances:
            video_url_appearances[src].append(url)
        else:
            video_url_appearances[src] = [url]

with open(output_file, "w") as file:
    for video_url, appearances in video_url_appearances.items():
        file.write(f"{video_url},{','.join(set(appearances))}\n")

print(f"\nDone, results in: {output_file}")
print(f"Found {len(video_url_appearances)} different videos on {len(urls)} pages")

winsound.Beep(250, 400)
winsound.Beep(250, 400)
