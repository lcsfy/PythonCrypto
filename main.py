import requests

def get_price(symbol):
    url = f"https://api.coinmarketcap.com/v2/ticker/{symbol}/?convert=EUR"
    response = requests.get(url)
    data = response.json()
    return data["data"]["quotes"]["EUR"]["price"]

top_5_symbols = [1, 2, 3, 4, 5]  # replace with actual symbol IDs
for symbol in top_5_symbols:
    price = get_price(symbol)
    print(f"Symbol ID: {symbol}, Price: {price} EUR")
