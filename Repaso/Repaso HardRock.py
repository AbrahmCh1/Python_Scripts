# SISTEMA DE REPASO DEL HARDROCK 06/09/2020 ABRAHAM CHÁVEZ YÁÑEZ
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


op = 1
costo = 0
bono = 1450


def menu(op):
    print("Menú de amenidades - Principal")
    print("1. Paseos")
    print("2. Spa")
    print(colored(255, 0, 0, "3. Salir del menú amenidades"))
    op = int(input("Elija una opción del menú: "))
    return (op)


def paseos():
    print("Menú de paseos")
    print("1.Paseo en yate 1000 dlls")
    print("2.Paseo en Kayak 300dlls")
    print(colored(255, 0, 0, "3.SALIR"))
    op_paseo = int(input(" Elija una opción del menu : "))
    if op_paseo == 1:
        return (1000)
    elif op_paseo == 2:
        return (300)
    else:
        return (0)


def spa():
    print("Menú del spa")
    print("1.Masaje Relajante 500 dlls")
    print("2.Limpieza facial 200 dlls")
    print(colored(255, 0, 0, "3.SALIR"))
    op_spa = int(input(" Elija una opción del menu : "))
    if op_spa == 1:
        return (500)  # masaje
    elif op_spa == 2:
        return (200)
    else:
        return (0)


print(" SISTEMA HARD ROCK PUERTO VALLARTA ")
noches = int(input("¿Cuántas noches desea hospedarse? "))
if noches >= 3:
    input("Tu bono de 1450 dlls fue asignado con éxito, presiona <ENTER> para usarlo")
    while op != 3:
        op = menu(op)
        if op == 1:  # selecciono paseos
            print(" MENÚ DE PASEOS ")
            costo = paseos()
            if bono >= costo and costo != 0:
                bono = bono-costo
                print("+ + RESERVACIÓN DEL PASEO CONFIRMADA + +")
                print(f"Se descontaron {costo}dlls del saldo de tu bono")
                input(f"Te quedan {bono}dlls de saldo <ENTER> para continuar")
            else:
                if costo != 0:  # significa que no tuviste saldo
                    print(
                        "Saldo insuficiente - te queda {bono}dlls en tu bono")
                    input(f"<ENTER> para continuar")
        elif op == 2:  # selecciono Spa
            print(" MENÚ DEL SPA ")
            costo = spa()
            if bono >= costo and costo != 0:
                bono = bono-costo
                print(" ++ RESERVACIÓN DEL SPA CONFIRMADA + + ")
                print(f" Se te descontaron {costo} dlls del saldo de tu bono")
                input(
                    f" Te quedan {bono} dlls de saldo <ENTER> para continuar")
            else:
                if costo != 0:  # significa que no tuviste saldo
                    print(
                        "Saldo insuficiente - te queda {bono}dlls en tu bono")
                    input(f"<ENTER> para continuar")

        else:
            if op == 3:
                print(f"Te quedaron {bono} dlls de saldo")
                input(f"<ENTER> para continuar")

            else:
                input("Opción Inválida, <ENTER> para continuar")
    print("Gracias por su visita")
else:
    print("No tienes derecho al bono, gracias por su visita!")
