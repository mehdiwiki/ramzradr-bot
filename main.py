import os
import time
import requests

TOKEN = os.getenv("TOKEN")
CHAT_ID = None  # بعداً میتونیم ذخیره کنیم

def get_price(symbol="BTCUSDT"):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    data = requests.get(url).json()
    return float(data["price"])

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": chat_id, "text": text})

last_price = None

while True:
    try:
        price = get_price()
        if last_price:
            change = ((price - last_price) / last_price) * 100
            if abs(change) >= 1:
                send_message(CHAT_ID, f"🚨 تغییر 1٪ در BTC\nقیمت: {price}")
        last_price = price
        time.sleep(60)
    except Exception as e:
        print("Error:", e)
        time.sleep(60)
