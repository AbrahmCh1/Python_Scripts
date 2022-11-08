# Práctica 4 Sistma de calificaciones Alumno excepcional
# Uso de lista y calculos
# ACY 23/09/2022
# ITESM
from tqdm import tqdm
from time import sleep

calificaciones = [97, 70, 55, 66, 100]
m = input("Ingresa tu matrícula: ")
print(
    f"\nLas calificaciones del alumno con matrícula {m} son: {calificaciones}")

for i in range(0, len(calificaciones)):
    if calificaciones[i]+5 < 100:
        calificaciones[i] = calificaciones[i] + 5
    elif calificaciones[i] >= 96 and calificaciones[i] < 100:
        s = 100-calificaciones[i]
        calificaciones[i] = calificaciones[i] + s

input("Presiona <ENTER> para ver tus nuevas calificaciones...")
for j in tqdm(range(100), desc="Progreso de actualización de calificaciones", colour="green"):
    sleep(0.01)
print(f"\nLas calificacioens NUEVAS son: {calificaciones}")
