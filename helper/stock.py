from pandas import DataFrame

# AAPL -> Apple
# MSFT -> Microsoft
# NVDA -> NVIDIA 
# TGT -> Target

def add_company_names():
    pass


if __name__ == "__main__":
    df = DataFrame({"symbol": ["AAPL", "MSFT", "NVDA", "TGT"]})
    print(df.head())

