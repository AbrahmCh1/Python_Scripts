#ACY 19/08/22
#propósito> Programa para comparar dos números enteros
#Problema Tarea 2- Condicionales
#ITESM

#Códigos de colores para la consola en Python
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
try: 

    print(GREEN+"****BIENVENIDO A TU COMPARADOR DE NUMEROS ENTEROS****")

    num1= int(input(YELLOW+"Ingresa tu primer número: "))
    num2= int(input("Ingresa tu segundo número: "))

    if num1 > num2 :
        print(CYAN+f"{num1} es mayor que {num2}"+RESET)
    elif num1 < num2 :
        print(CYAN+f"{num2} es mayor que {num1}"+RESET)
    elif num1 == num2 :
        print(CYAN+"Tus números son iguales"+RESET)
   
except:
    print(RED+"Error de tipo de dato, contacta al administrador del sistema"+RESET)

