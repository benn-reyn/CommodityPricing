

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self._create_tables()

    def _create_connection(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row 
        return conn

    def _create_tables(self):
        with self._create_connection() as conn:
            cursor = conn.cursor()

            cursor.executescript("""
                CREATE TABLE IF NOT EXISTS commodity_prices (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    commodity TEXT NOT NULL,
                    symbol TEXT NOT NULL,
                    price REAL NOT NULL,
                    currency TEXT DEFAULT 'USD',
                    volume REAL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    source TEXT DEFAULT 'yfinance',
                    metadata TEXT,
                    UNIQUE(symbol, timestamp)
                );

                CREATE TABLE IF NOT EXISTS commodity_stocks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category TEXT NOT NULL,
                    company_name TEXT,
                    symbol TEXT NOT NULL,
                    price REAL NOT NULL,
                    currency TEXT DEFAULT 'USD',
                    volume REAL,
                    market_cap REAL,
                    dividend_yield REAL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    source TEXT DEFAULT 'yfinance',
                    metadata TEXT,
                    UNIQUE(symbol, timestamp)
                );

                CREATE TABLE IF NOT EXISTS commodity_exposures (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    company_symbol TEXT NOT NULL,
                    commodity_type TEXT NOT NULL,
                    exposure_level TEXT,
                    revenue_percentage REAL,
                    UNIQUE(company_symbol, commodity_type)
                );

                CREATE INDEX IF NOT EXISTS idx_stocks_category ON commodity_stocks(category);
                CREATE INDEX IF NOT EXISTS idx_exposures_company ON commodity_exposures(company_symbol);
            """)
            print("Tables created")

    def get_latest_prices(self):
        with self._create_connection() as conn:
            cursor = conn.cursor()

            query = """
            SELECT
                symbol,
                commodity AS name,
                price,
                currency,
                volume,
                timestamp,
                source,
                metadata,
                'commodity' AS type
            FROM commodity_prices
            WHERE (symbol, timestamp) IN (
                SELECT symbol, MAX(timestamp)
                FROM commodity_prices
                GROUP BY symbol
            )

            UNION ALL

            SELECT
                symbol,
                company_name AS name,
                price,
                currency,
                volume,
                timestamp,
                source,
                metadata,
                'stock' AS type
            FROM commodity_stocks
            WHERE (symbol, timestamp) IN (
                SELECT symbol, MAX(timestamp)
                FROM commodity_stocks
                GROUP BY symbol
            )
            """

            rows = cursor.execute(query).fetchall()
            return [dict(row) for row in rows]


if __name__ == "__main__":
    db = DatabaseManager("commodity_prices.db")
    prices = db.get_latest_prices()
    print(f"Retrieved {len(prices)} latest prices.")
    print(prices[:3])
