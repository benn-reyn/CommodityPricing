def fetch_and_store(db: SimpleDatabaseManager):
    print("Fetching news sentiment")
    try:
        url = f"https://newsapi.org/v2/everything?q=commodities&apiKey={Config.NEWS_API_KEY}"
        resp = requests.get(url)
        if resp.status_code == 200:
            articles = resp.json().get("articles", [])
            for article in articles[:5]: 
                title = article.get("title")
                description = article.get("description")
                published = article.get("publishedAt")
                db.insert_news_article(title, description, published)
            print(f"Retrieved {len(articles[:5])} news articles")
        else:
            print(f"NewsAPI error: {resp.status_code}")
    except Exception as e:
        print(f"News ingestion failed: {e}")

if __name__ == "__main__":
    db = SimpleDatabaseManager(Config.DATABASE_PATH)
    fetch_and_store(db)
