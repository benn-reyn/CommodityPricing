def fetch_and_store(db: SimpleDatabaseManager):
    print("Fetching World Bank data")
    try:
        url = f"https://api.worldbank.org/v2/en/indicator/FP.CPI.TOTL?format=json"
        resp = requests.get(url)
        if resp.status_code == 200:
            data = resp.json()
            if len(data) > 1:
                latest = data[1][0]
                price = latest.get("value")
                db.insert_commodity_price("world_bank_cpi", "FP.CPI.TOTL", price)
                print(f"World Bank CPI: {price}")
        else:
            print(f"World Bank API error: {resp.status_code}")
    except Exception as e:
        print(f"World Bank ingestion failed: {e}")

if __name__ == "__main__":
    db = SimpleDatabaseManager(Config.DATABASE_PATH)
    fetch_and_store(db)
