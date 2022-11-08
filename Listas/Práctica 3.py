# ACY 23/09/22
# Práctica 3 Sistema de panadería
# ITESM
from tqdm import tqdm
from time import sleep
import winsound

winsound.Beep(1000, 500)
winsound.Beep(2000, 600)

print("- SISTEMA DE LA PANADERÍA LOS ALTOS - ALTA DE PRODUCTOS -")
print("          * * *Alta de productos* * *\n")

panes = []
c = int(input("¿Cuántos tipos de panes llegaron hoy? "))
for i in range(c):
    panes.append(input(f"Nombre del pan {i+1}: "))

print("\nEspere  mientras se capturan los panes en la base de datos...")
for i in tqdm(range(100), desc="Progreso de actualización de los panes", colour="red"):
    sleep(0.01)

print(f"\nLos panes capturados el día de hoy fueron {panes}")
