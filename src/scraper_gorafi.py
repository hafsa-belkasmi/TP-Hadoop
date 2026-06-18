import requests
from bs4 import BeautifulSoup

def scrape_gorafi():
    url = "https://www.legorafi.fr/"
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
                "source": "Le Gorafi",
                "url": url,
                "label": "FAKE"
            })

    return articles


if __name__ == "__main__":
    articles = scrape_gorafi()

    for article in articles:
        print(article)