# Practica 1 Matrices 3x4

matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# forma 1
print("Forma 1")
print(matriz)

# forma 2
print("\nForma 2")
print(*matriz, sep="\n")

# forma 3
print("\nForma 3")
for i in matriz:
    print(i)

# forma 4
print("\nForma 4")
busca = False
n = int(input("Que número quieres buscar? "))
for fila in matriz:
    for columna in fila:
        if columna == n:
            busca = True
if busca == True:
    print(*matriz, sep="\n")
    print(f"Esta matriz si contiene el numero {n}")
