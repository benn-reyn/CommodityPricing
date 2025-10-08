load_dotenv()

class Config:
    DATABASE_PATH = 'commodity_prices.db'
    
    #creates dict of commodity ticker symbol
    COMMODITIES = {
        # PRECIOUS METALS
        'gold': ['GC=F', 'GLD'],                    # Futures + ETF
        'silver': ['SI=F', 'SLV'],                  # Futures + ETF
        'platinum': ['PL=F', 'PPLT'],               # Futures + ETF
        'palladium': ['PA=F', 'PALL'],              # Futures + ETF
        
        # ENERGY
        'crude_oil': ['CL=F', 'USO'],               # WTI Crude
        'brent_oil': ['BZ=F', 'BNO'],               # Brent Crude
        'natural_gas': ['NG=F', 'UNG'],             # Nat Gas
        'gasoline': ['RB=F'],                       # RBOB Gasoline
        'heating_oil': ['HO=F'],                    # Heating Oil
        
        # INDUSTRIAL METALS
        'copper': ['HG=F', 'CPER'],                 # Copper
        'aluminum': ['ALI=F'],                      # Aluminum
        'zinc': ['ZN=F'],                           # Zinc
        'nickel': ['NIL=F'],                        # Nickel
        'lead': ['LED=F'],                          # Lead
        'tin': ['SNEEF'],                           # Tin
        
        # AGRICULTURE
        'corn': ['ZC=F', 'CORN'],                   # Corn
        'wheat': ['ZW=F', 'WEAT'],                  # Wheat
        'soybeans': ['ZS=F', 'SOYB'],               # Soybeans
        'soybean_oil': ['ZL=F'],                    # Soybean Oil
        'soybean_meal': ['ZM=F'],                   # Soybean Meal
        'cotton': ['CT=F', 'BAL'],                  # Cotton
        'coffee': ['KC=F', 'JO'],                   # Coffee
        'sugar': ['SB=F', 'CANE'],                  # Sugar
        'cocoa': ['CC=F'],                          # Cocoa
        'live_cattle': ['LE=F'],                    # Live Cattle
        'lean_hogs': ['HE=F'],                      # Lean Hogs
        
        # SOFT COMMODITIES
        'lumber': ['LBS=F'],                        # Lumber
        'orange_juice': ['OJ=F'],                   # Orange Juice
    }
    
    # COMMODITY-PRODUCING COMPANIES (STEEL, MINING, ENERGY)
    COMMODITY_STOCKS = {
        # STEEL PRODUCERS
        'steel_producers': ['NUE', 'X', 'STLD', 'CLF', 'RS'],
        
        # COPPER MINERS
        'copper_miners': ['FCX', 'SCCO', 'TECK', 'RIO', 'BHP'],
        
        # GOLD MINERS  
        'gold_miners': ['NEM', 'GOLD', 'AEM', 'KL', 'WPM'],
        
        # SILVER MINERS
        'silver_miners': ['AG', 'PAAS', 'EXK', 'MAG', 'CDE'],
        
        # ENERGY COMPANIES
        'energy_companies': ['XOM', 'CVX', 'COP', 'EOG', 'PXD'],
        
        # AGRICULTURE COMPANIES
        'agriculture_companies': ['ADM', 'BG', 'TSN', 'MOS', 'CF'],
        
        # INDUSTRIAL METAL MINERS
        'diversified_miners': ['VALE', 'RIO', 'BHP', 'GLNCY'],
    }
    
    COLLECTION_INTERVAL = 30
    VALUATION_THRESHOLD = 1.5

print("Commodity market established")
print(f"Now tracking: {len(Config.COMMODITIES)} commodity types")
print(f"And: {len(Config.COMMODITY_STOCKS)} commodity stock categories")
