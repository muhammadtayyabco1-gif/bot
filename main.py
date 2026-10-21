import requests, time, threading
from flask import Flask
BOT_TOKEN="8201871814:AAGuHPJfxpIOAM-WTOPVO7UHc8TZkbLucR0"
CHAT_ID="8357894020"
COINS=["BTCUSDT","ETHUSDT","BNBUSDT","SOLUSDT","XRPUSDT","ADAUSDT","DOGEUSDT","SHIBUSDT","AVAXUSDT","DOTUSDT","LINKUSDT","LTCUSDT","TRXUSDT","MATICUSDT","BCHUSDT","UNIUSDT","XLMUSDT","ETCUSDT","FILUSDT","ICPUSDT","APTUSDT","NEARUSDT","ARBUSDT","PEPEUSDT","OPUSDT","INJUSDT","SUIUSDT","RNDRUSDT","FETUSDT","WIFUSDT"]
base_prices={}
app=Flask(__name__)
@app.route('/')
def home():return "Bot Running 0.6%"
def send(m):
 try:requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",data={"chat_id":CHAT_ID,"text":m},timeout=15)
 except:pass
def get_price(s):
 try:return float(requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={s}",timeout=10).json()['price'])
 except:return None
def run_bot():
 send("✅ CLOUD BOT STARTED - 24/7 Live - 0.6% Filter")
 last=time.time()
 while True:
  try:
   if time.time()-last>3600:base_prices.clear();last=time.time()
   for coin in COINS:
    price=get_price(coin)
    if price:
     if coin not in base_prices:base_prices[coin]=price
     else:
      ch=((price-base_prices[coin])/base_prices[coin])*100
      if ch>=0.6:
       sl=price-(price*0.015);tp=price+(price*0.03)
       send(f"🚀 BUY: {coin}\nPump: +{ch:.2f}%\nEntry: {price}\nSL: {sl:.4f}\nTP: {tp:.4f}\nLeverage: 5x-10x")
       base_prices[coin]=price
    time.sleep(0.4)
   time.sleep(10)
  except:time.sleep(5)
threading.Thread(target=run_bot,daemon=True).start()
if __name__=="__main__":app.run(host='0.0.0.0',port=10000)
