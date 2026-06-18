import pandas as pd
from scraper_gorafi import scrape_gorafi
from detector import detect_fake_news

articles = scrape_gorafi()

for article in articles:
    text = article["title"] + " " + article["summary"]
    article["prediction"] = detect_fake_news(text)

df = pd.DataFrame(articles)

df.to_csv("data/news.csv", index=False)

print("CSV créé : data/news.csv")
print(df)