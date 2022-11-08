from tabulate import tabulate as tab

calificaciones = [
    [100, 80, 90, 56],
    [90, 70, 78, 90],
    [90, 95, 100, 90]
]

encabezado = ["Matemáticas", "Español", "Ciencias", "Deportes"]


print(tab(calificaciones, headers=encabezado, tablefmt="fancy_grid",
      colalign=("center", "center", "center", "center")))
