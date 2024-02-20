# Importar las librerías necesarias
import requests
import json

n = float(input("Ingrese la cantidad de bitcoins que posee: "))

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    print("Ocurrió un error al consultar la API")
    exit()

data = response.json()

price = data["bpi"]["USD"]["rate_float"]

cost = price * n

cost = format(cost, ",.4f")

print(f"El costo actual de {n} bitcoins en USD es ${cost}")
