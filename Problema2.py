# Importar las librerías necesarias
from pyfiglet import Figlet
import random

figlet = Figlet()

font = input("Ingrese el nombre de una fuente, o presione enter para seleccionar una al azar: ")

fonts = figlet.getFonts()

if font in fonts:
    print(f"Usando la fuente {font}")
else:
    font = random.choice(fonts)
    print(f"Fuente no encontrada, usando la fuente {font}")

text = input("Ingrese un texto a imprimir: ")

figlet.setFont(font=font)

ascii_art = figlet.renderText(text)

print(ascii_art)
