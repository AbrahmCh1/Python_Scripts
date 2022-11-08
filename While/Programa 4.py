#ACY 26/08/22
#Programa 4 ahorro
#Ultima Modificación 26/08/2022
#ITESM
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

suma=0
dias=1

while (dias <= 7):
    cantidad = int(input(colored(255,147,255, "¿Cuánto ahorraste hoy Juanita? $")))
    suma = suma+ cantidad
    print(colored(0, 210, 120, f"Llevas ${suma} ahorrado, hasta ahorita has ahorrado {dias} días"))
    dias=dias+1
print(colored(255, 128, 0, f"\t\nFelicidades Juanita ahorraste ${suma} esta semana"))