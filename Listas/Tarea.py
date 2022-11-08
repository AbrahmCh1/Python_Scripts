# Programa para una agencia de empleos
# ACY 23/09/22
# ITESM

from tqdm import tqdm
from time import sleep
import random
from termcolor import colored

RED = "\033[1;31m"
RESET = "\033[0;0m"

print("- AGENCIA DE EMPLEOS - CONTRATACIONES -\n")
cont = int(input("¿Cuántas personas se registraron hoy? "))
Candidatos = []

for i in range(cont):
    Candidatos.append(str(input(f"Nombre del candidato {i+1}: ")))

print("\nEspere mientras se capturan los nombres en la base de datos...")

print(RED)
for k in tqdm(range(100), desc="Actualizando nombres: "):
    sleep(0.01)

print(f"\n\n\n\nLos empleados entrevistados fueron: {Candidatos}")
print(colored(
    f"\nEl candidato {random.choice(Candidatos)} es el que ganó la vacante!", "yellow"))
