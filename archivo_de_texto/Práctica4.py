import os

archivo = open("puntaje.txt", "a")
print("El archivo fue abierto como agregar datos")

nombre = str(input("Nombre del jugador: "))
datos_jugador = ["\n07/10/2022", "-", nombre, "-Minecraft-", "100 puntos"]

archivo.writelines(datos_jugador)
print("Lista agregada exitosamente")

archivo = open("puntaje.txt", "r")
contenido = archivo.read()

print(contenido)

archivo.close()
print("El archivo se cerró")
