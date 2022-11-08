import os

archivo = open("puntaje.txt", "r")

lalinea = 1

for linea in archivo.readlines():
    if "John" in linea:
        print("* * * * * * John fue encontrado * * * * * *")
    else:
        print(lalinea, linea, end="")
    lalinea = lalinea + 1

archivo.close()
