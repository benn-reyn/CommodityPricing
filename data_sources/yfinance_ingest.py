def fetch_and_store(db: SimpleDatabaseManager):
    print("Fetching data from YF")
    for commodity, symbols in Config.COMMODITIES.items():
        for symbol in symbols:
            try:
                ticker = yf.Ticker(symbol)
                hist = ticker.history(period="1d")
                if not hist.empty:
                    price = hist['Close'][-1]
                    volume = hist['Volume'][-1]
                    db.insert_commodity_price(commodity, symbol, price, volume)
                    print(f"{commodity} ({symbol}): {price}")
            except Exception as e:
                print(f"Error fetching YF {symbol}: {e}")

if __name__ == "__main__":
    db = SimpleDatabaseManager(Config.DATABASE_PATH)
    fetch_and_store(db)
