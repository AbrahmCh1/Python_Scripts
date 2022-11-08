#ACY 23/08/22
#Programa de acuario
#Ultima Modificación 23/08/22
#ITESM
from datetime import datetime #Importa la fecha
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def total(n1,n2): #Define la funcion total y se ingresarán dos datos (número 1, número 2)
    pa_dulce = dulce*200 #Variable interna pa_dulce es igual a la variable general dulce por 200
    pa_salada = salado*500 #Variable interna pa_salada es igual a la variable general salado por 500
    return(pa_dulce+pa_salada) #Regresa al código general la suma de pa_dulce + pa_salada

print(colored(210,255,0,"********BIENVENDIDO AL SISTEMA DE ACUARIO AQUA********"))
date = datetime.now()
print(colored(0, 0, 255, f"\nHoy estamos a {date}"))

opciones = print(colored(204, 504, 0, "- - - TENEMOS ESTE TIPO DE PECES - - -"), "\n\tAgua dulce $200 c/u", "\n\tAgua salada $500 c/u")

dulce= int(input(colored(122,117,0, "¿Cuántos peces de agua dulce llevará? ")))
salado= int(input(colored(122, 117, 0, "¿Cuántos peces de agua salada llevará? ")))

calc= total(dulce,salado) #Inicializa variable calc y llama a la función total mandandole los datos de dulce y de salado
print(colored(0, 204, 204, f"Peces de agua dulce: {dulce} >>>>> ${dulce*200}"))
print(colored(0, 204, 204, f"Peces de agua salada: {salado} >>>>> ${salado*500}"))
print(colored(0, 0, 255, "Su total es de: $"),calc)

if calc > 1500: #Si la variable Calc que es la que iguala a la funcion total es mayor a 1500 pasa lo siguiente:
    print(colored(0, 255, 255, "\nFELICIDADES HAS COMPRADO MÁS DE $1500 Y HAS GANADO UN PREMIO"))
    print(colored(0, 102, 204, "\n¿CUÁL QUIERES?: "), "\n\tOpción 1: Un pez extra de agua dulce [1]", "\n\tOpción 2: Alimento vivo [2]", "\n\tOpción 3: Limpieza de pecera gratis! [3]" )
    
    while True: 
        premio = int(input(colored(255 , 0, 127, "ELIGE UNA OPCIÓN [1]      [2]     [3]")))
        if premio == 1:
            print(colored(51, 255, 133, "Elegiste >>>>>> Un pez extra de agua dulce"))
            print("\n\tMuchas gracias por su compra, vuelva pronto :D")
            break
        elif premio == 2:
            print(colored(51,255,133, "Elegiste >>>>>> Alimento vivo"))
            print("\n\tMuchas gracias por su compra, vuelva pronto :D")
            break
        elif premio == 3:
            print(colored(51, 255, 133, "Elegiste >>>>>> Limpieza de pecera gratis!"))
            print("\n\tMuchas gracias por su compra, vuelva pronto :D")
            break
        print("Intentalo de nuevo")
    
else:
    print("\n\tMuchas gracias por su compra, vuelva pronto :D")




