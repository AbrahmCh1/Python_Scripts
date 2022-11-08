#Ejercicio 1 for con range 30/08/2022 ACY
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

cantidad = 20

for i in range(cantidad):
    print(f"El celular modelo {i+1} ha sido ensamblado con éxito")
    if i == 4:
        print(colored(255,0,0,f"El celular modelo {i+1} está defectuoso"))