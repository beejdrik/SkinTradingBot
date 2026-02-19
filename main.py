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
        deals = []
        for item in skinPortItems:
            if item['suggested_price'] is None:
                continue
            if item['min_price'] < .77 * item['suggested_price'] and item['quantity'] > 10 and item['min_price'] > 3.00:
                discount_pct = (1 - item['min_price'] / item['suggested_price']) * 100
                deals.append((discount_pct, item))

        deals.sort(key=lambda x: x[0], reverse=True)

        for discount_pct, item in deals:
            print(f"{item['market_hash_name']} | Min: ${item['min_price']} | Suggested: ${item['suggested_price']} | Discount: {discount_pct:.1f}%")
    print("Waiting 5 minutes...")
    time.sleep(300)
