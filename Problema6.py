# Definir la función que cuenta las líneas de código de un archivo .py
def contar_lineas(ruta):
    try:
        archivo = open(ruta, "r")
        lineas = archivo.readlines()
        archivo.close()
    except FileNotFoundError:
        print("La ruta es inválida o el archivo no existe")
        return None
    contador = 0
    for linea in lineas:
        linea = linea.strip()
        longitud = len(linea)
        primer_caracter = linea[0] if longitud > 0 else ""
        if longitud > 0 and primer_caracter != "#":
            contador += 1
    return contador

ruta = input("Ingrese la ruta de un archivo .py (nombre y ruta): ")

if ruta.endswith(".py"):
    resultado = contar_lineas(ruta)
    print(f"El archivo {ruta} tiene {resultado} líneas de código válidas")
else:
    print("El nombre del archivo debe terminar en .py")
