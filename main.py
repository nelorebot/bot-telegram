import requests
import schedule
import time

TOKEN = "8676569640:AAF7Lbdj1thUHOd3SJ5DgvgjdHo_tRYEnUQ"
CHAT_ID = "8337438097"

def enviar_mensagem():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": "🔥 Bot online 24h funcionando!"
    }
    requests.post(url, data=payload)

schedule.every().day.at("10:00").do(enviar_mensagem)

while True:
    schedule.run_pending()
    time.sleep(1)
