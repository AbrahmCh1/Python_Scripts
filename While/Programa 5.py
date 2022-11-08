# ACY 26/08/22
# Programa 5 menú de operaciones con ciclo
# Ultima Modificación 26/08/2022
# ITESM
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


op = 0
while (op != 3):
    print(colored(128, 128, 128,
          "****************************************************************"))
    print("\t\tMENÚ DE OPERACIONES")
    print(colored(0, 145, 125, "Estas son las operaciones disponibles:"))
    print(colored(0, 255, 0, "\t 1.Calcular el area"), end="")
    print(colored(0, 255, 0, "\t 2.Calcular el perimetro"))
    print(colored(255, 0, 0, "\t\t 3. SALIR DEL MENÚ"))
    op = int(input(colored(0, 0, 255, "\nEscribe el número de operación deseada")))

print("Fin del menú, aquí inicia otra cosa del programa")
