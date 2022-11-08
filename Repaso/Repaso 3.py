# ACY 02/09/22
# Programa
# ITESM
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


try:
    n = int(input("¿Cuántos masajes desea contratar?"))
    suma = 0
    for i in range(n):
        continuar = str(
            input(f"Su masaje {i+1} terminó, Continuar [SI][NO]: "))
        if continuar.upper() == "NO":
            print(colored(255, 0, 0, "Su servicio se suspendió por decisión propia!"))
            break
        else:
            suma += 1

    if suma != n:
        print(
            f"Lamentamos los inconvenientes, recibió {i+1} de sus {n} masajes ")
    else:
        print(colored(0, 255, 0, "\nGracias por su preferencia, vuelva pronto"))
    input("Presiones <ENTER> para terminar y pasar a caja a hacer el pago")
except:
    print(colored(255, 0, 0, "Error de entrada, llame al administrador"))
