def normalize_year(year):
    return int(year)

def normalize_ticker(ticker):
    return str(ticker).strip().upper()

def normalize_text(text):
    return str(text).strip()

def normalize_float(value):
    if value is None or value == "":
        return 0.0
    return float(value)