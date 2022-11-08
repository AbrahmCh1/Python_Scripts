#Ejercicio2 for con range 30/08/2022 ACY
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

vacantes = int(input("¿Cuántas vacantes disponibles hay el día de hoy? "))

for i in range (1,vacantes+1):
    print(f"La vacante {i} ya fue asignada")
    input("Presione <ENTER> para continuar\n")
print(colored(45,124,75,"\n\t El personal ha sido contratado y firmado el contrato laboral"))
