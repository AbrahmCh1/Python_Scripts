
matriz = []

f = int(input("Cuantas filas quieres? "))
c = int(input("Cuantas columnas quieres? "))

for fila in range(f):
    lista = []
    for columna in range(c):
        letra = str(
            lista.append(input(f"Dame la letra de la fila {fila} y columna {columna}: ")))
    matriz.append(lista)

print(*matriz, sep="\n")
