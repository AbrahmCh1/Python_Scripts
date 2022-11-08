# Programa para buscar una letra en un título y regresar cuantas veces aparece
# ACY
# 20/09/2022
# ITESM
cancion = str.lower(input("Ingresa el nombre de tu canción favorita: "))
lets = str.lower(input("Letra a buscar: "))
c = 0


for letra in cancion:
    if letra == lets:
        print("Letra encontrada")
        c += 1

if c != 1:
    print(f"Tu título tiene la letra '{lets.upper()}' {c} veces")
else:
    print(f"Tu título tiene la letra '{lets.upper()}' {c} vez")
