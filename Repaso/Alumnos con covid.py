# ACY 02/09/22
# Programa que muestra cuantos alumnos tienen covid y cuantos no
# ITESM


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


print(colored(0, 145, 0, "- AGENCIA DE EMPLEOS - CONTRATACIONES -"))
cont = int(input("¿Cuántas personas se registraron hoy? "))
Candidatos = []
