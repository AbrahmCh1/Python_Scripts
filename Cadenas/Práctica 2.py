# Programa para regresar una palabra en regresión
# ACY
# 20/09/2022
# ITESM

clave = str(input("Dime una clave secreta: "))

for f in range(len(clave), 0, -1):
    print(clave[f-1], end="")
