#ACY 26/08/22
#Programa 3
#Ultima Modificación 26/08/2022
#ITESM
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
km = 0
while(km<10):
    kmhoy = int(input(colored(0,0,255,"¿Cuántos kilometros recorriste hoy?")))
    km = km+ kmhoy
    print(colored(120, 255, 120, f"Llevas {kmhoy} recorridos, sigue entrenando!"))

print("\tFIN DEL ENRENAMIENTO, ESTAS LISTO PARA EL MARATON")