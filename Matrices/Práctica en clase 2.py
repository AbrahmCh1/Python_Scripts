matriz = []

for fila in range(3):
    lista = []
    for columna in range(4):
        numero = lista.append(
            int(input(f"Introduce el valor de la fila {fila} y columna {columna}: ")))
    matriz.append(lista)

print(*matriz, sep="\n")
