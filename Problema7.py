# Importar las librerías necesarias
import requests
import sqlite3

conn = sqlite3.connect("base.db")

cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS sunat_info (fecha TEXT, compra REAL, venta REAL)")

for mes in range(1, 13):
    url = f"https://api.apis.net.pe/v1/tipo-cambio-sunat?month={mes}&year=2023"

    response = requests.get(url)

    try:
        data = response.json()

        cambio = data["cambio"]

        for c in cambio:
            fecha = c[0]
            compra = c[1]
            venta = c[2]
            cur.execute("INSERT INTO sunat_info VALUES (?, ?, ?)", (fecha, compra, venta))
    except TypeError:
        print("La respuesta del API no es válida")

conn.commit()

cur.execute("SELECT * FROM sunat_info")

resultados = cur.fetchall()

cur.close()
conn.close()

for r in resultados:
    print(r)
