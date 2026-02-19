import requests
import time

url = "https://api.skinport.com/v1/items"
params = {
    "app_id": 730,
    "currency": "USD"
}

headers = {
    "Accept-Encoding": "br",
    "User-Agent": "SkinTradingBot/1.0"
}

while True:
    response = requests.get(url, params=params, headers=headers)
    skinPortItems = response.json()

    if response.status_code != 200:
        print(f"Error: {response.status_code} - {skinPortItems}")
    else:
        for item in skinPortItems:
            if item['suggested_price'] is None:
              continue
            if item['min_price'] < .77 * item['suggested_price'] and item['quanity'] > 10 and item['min_price'] > 3.00:
                print(f"{item['market_hash_name']} | Min: ${item['min_price']} | Suggested: ${item['suggested_price']}")
    print("Waiting 5 minutes...")
    time.sleep(300)
