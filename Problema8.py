import requests
import sqlite3
import datetime

conn = sqlite3.connect("base.db")

cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS bitcoin (fecha TEXT, usd REAL, gbp REAL, eur REAL, pen REAL)")

url_bitcoin = "https://api.coindesk.com/v1/bpi/currentprice.json?currency=USD,GBP,EUR"

response_bitcoin = requests.get(url_bitcoin)

data_bitcoin = response_bitcoin.json()

usd = data_bitcoin["bpi"]["USD"]
gbp = data_bitcoin["bpi"]["GBP"]
eur = data_bitcoin["bpi"]["EUR"]

usd = usd["rate_float"]
gbp = gbp["rate_float"]
eur = eur["rate_float"]

url_sunat = "https://api.apis.net.pe/v1/tipo-cambio-sunat"

fecha = datetime.date.today().isoformat()

url_sunat = url_sunat + "?fecha=" + fecha

response_sunat = requests.get(url_sunat)

data_sunat = response_sunat.json()

venta = data_sunat["venta"]

pen = usd * venta

cur.execute("INSERT INTO bitcoin VALUES (?, ?, ?, ?, ?)", (fecha, usd, gbp, eur, pen))

conn.commit()

cur.execute("SELECT * FROM bitcoin")

resultados = cur.fetchall()

cur.close()
conn.close()

for r in resultados:
    print(r)

pen_10 = pen * 10
eur_10 = eur * 10

print(f"El precio de comprar 10 bitcoins en moneda PEN es {pen_10:.2f} soles")
print(f"El precio de comprar 10 bitcoins en moneda EUR es {eur_10:.2f} euros")
