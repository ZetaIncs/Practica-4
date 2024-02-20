# Definir la función que guarda la tabla de multiplicar de un número en un fichero
def guardar_tabla(n):
    fichero = open(f"tabla-{n}.txt", "w")
    for i in range(1, 11):
        fichero.write(f"{n} x {i} = {n*i}\n")
    fichero.close()

def mostrar_tabla(n):
    try:
        fichero = open(f"tabla-{n}.txt", "r")
        contenido = fichero.read()
        fichero.close()
        print(contenido)
    except FileNotFoundError:
        print(f"No se encontró el fichero tabla-{n}.txt")

def mostrar_linea(n, m):
    try:
        fichero = open(f"tabla-{n}.txt", "r")
        lineas = fichero.readlines()
        fichero.close()
        linea = lineas[m-1]
        print(linea)
    except FileNotFoundError:
        print(f"No se encontró el fichero tabla-{n}.txt")

menu = """
Menú de opciones:
1. Guardar la tabla de multiplicar de un número en un fichero
2. Mostrar la tabla de multiplicar de un número desde un fichero
3. Mostrar una línea de la tabla de multiplicar de un número desde un fichero
4. Salir
"""

opcion = 0
while opcion != 4:
    print(menu)
    opcion = input("Elija una opción: ")
    opcion = int(opcion)
    if opcion == 1:
        n = input("Ingrese un número entre 1 y 10: ")
        n = int(n)
        if 1 <= n <= 10:
            guardar_tabla(n)
            print(f"Se guardó la tabla de multiplicar del {n} en el fichero tabla-{n}.txt")
        else:
            print("El número debe estar entre 1 y 10")
    elif opcion == 2:
        n = input("Ingrese un número entre 1 y 10: ")
        n = int(n)
        if 1 <= n <= 10:
            mostrar_tabla(n)
        else:
            print("El número debe estar entre 1 y 10")
    elif opcion == 3:
        n = input("Ingrese el primer número entre 1 y 10: ")
        m = input("Ingrese el segundo número entre 1 y 10: ")
        n = int(n)
        m = int(m)
        if 1 <= n <= 10 and 1 <= m <= 10:
            mostrar_linea(n, m)
        else:
            print("Los números deben estar entre 1 y 10")
    elif opcion == 4:
        print("Gracias por usar el programa. Hasta pronto.")
    else:
        print("La opción debe ser un número entre 1 y 4")