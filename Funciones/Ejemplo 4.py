#ACY 23/08/2022
#Ejemplo de una función CON ENVIO DE PARAMETROS Y RETORNO DE VALORE EN UN MENU DE OPERACIONES
#Programa que sirve para restar 2 numero inicializados por el usuario
#ITESM
#codigo para ingresar rgb en la consola de python
from datetime import datetime

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def main (num1,num2, letra):
    if letra == "s":
        return(num1+num2)
    elif letra == "r":
        return(num1-num2)
    elif letra == "m":
        return(num1*num2)
    elif letra == "d":
        return(num1/num2)
    else:
        print(colored(255,0,0, "Letra invalida, no corresponde a ninguna operación"))

hoy= datetime.now()

print("****** MENÚ DE OPERACIONES ******")
print(colored(0, 255, 0, hoy))

valor1= int(input(colored(127,52,112, "Dame el valor 1: ")))
valor2= int(input(colored(127,52,112, "Dame el valor 2: ")))
print(colored(142,155,230, "Indica la operacion que deseas realizar con los numeros: "))
print(colored(117,118,124,"\t Calcular la suma [s]"))
print(colored(117,118,124,"\t Calcular la resta [r]"))
print(colored(117,118,124,"\t Calcular la multiplicación [m]"))
print(colored(117,118,124,"\t Calcular la división [d]"))

op= str.lower(input("Indica la letra de la operacion deseada: "))

print(colored(224,147,114, "El resultado de la operacion es"), main(valor1, valor2, op))
