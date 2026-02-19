import requests
import time
import brotli  # noqa: F401 - enables automatic brotli decompression in urllib3

url = "https://api.skinport.com/v1/items"
params = {"app_id": 730, "currency": "USD"}

headers = {"Accept-Encoding": "br", "User-Agent": "SkinTradingBot/1.0"}

while True:
    try:
        response = requests.get(url, params=params, headers=headers)

        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text[:200]}")
        else:
            skinPortItems = response.json()

undervalued = []
for item in skinPortItems:
    if item['suggested_price'] is None:
        continue
    if item['min_price'] < .77 * item['suggested_price'] and item['quantity'] > 10 and item['min_price'] > 3.00:
        undervalued.append(item)

# Sort by how undervalued they are (lowest ratio = greatest discount)
undervalued.sort(key=lambda x: x['min_price'] / x['suggested_price'])

for item in undervalued:
    ratio = item['min_price'] / item['suggested_price']
    print(
        f"{item['market_hash_name']} | Min: ${item['min_price']} | Suggested: ${item['suggested_price']} | {ratio:.1%} of suggested"
    )
    except Exception as e:
        print(f"Request failed: {e}")

    print("Waiting 5 minutes...")
    time.sleep(300)
