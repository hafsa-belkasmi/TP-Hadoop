import pandas as pd
from scraper_gorafi import scrape_gorafi
from scraper_franceinfo import scrape_franceinfo
from detector import detect_fake_news

def main():
    articles = scrape_gorafi() + scrape_franceinfo()

    for article in articles:
        text = article["title"] + " " + article["summary"]
        article["prediction"] = detect_fake_news(text)

    df = pd.DataFrame(articles)
    df.to_csv("data/news.csv", index=False)

    print("CSV créé : data/news.csv")
    print(df)

if __name__ == "__main__":
    main()