# Práctica 2
# Abraham Chávez Yáñez
# Abrir archivo y agregar datos
import os

archivo = open("log_del_juego.txt", "a")
print("El archivo fue abierto y está listo para recibir datos")

nombre = str(input("¿Nombre del jugador?"))
edad = str(input("Edad del jugador: "))
print("\nFisica")
print("\nMatematicas")
print("\nCiencias")
area = str(input("¿En que area desea jugar?"))

archivo.write("\n" + nombre)
archivo.write("\n" + edad)
archivo.write("\n" + area + "\n")

archivo.close()
