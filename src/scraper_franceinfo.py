import requests
from bs4 import BeautifulSoup

def scrape_franceinfo():
    url = "https://www.francetvinfo.fr/"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = []

    titles = soup.find_all(["h1", "h2", "h3"])

    for title in titles[:10]:
        text = title.get_text(" ", strip=True)

        if text and len(text) > 20:
            articles.append({
                "title": text,
                "summary": text,
                "source": "France Info",
                "url": url,
                "label": "REAL"
            })

    return articles