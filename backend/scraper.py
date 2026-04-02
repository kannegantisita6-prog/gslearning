import requests
from bs4 import BeautifulSoup
import json

BASE = "https://www.mygreatlearning.com"

def scrape():
    url = f"{BASE}/academy"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    courses = []

    for a in soup.find_all("a"):
        href = a.get("href")
        title = a.text.strip()

        if href and "/courses/" in href and title:
            full_url = BASE + href if href.startswith("/") else href

            courses.append({
                "title": title,
                "url": full_url,
                "brand": "YourBrand"
            })

    unique = {c['url']: c for c in courses}.values()

    with open("courses.json", "w") as f:
        json.dump(list(unique), f, indent=2)

if __name__ == "__main__":
    scrape()
