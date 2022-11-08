#ACY 19/08/22
#propósito> Programa para identificar si un numero es par o impar
#Problema Tarea 1- Condicionales
#ITESM
YELLOW = '\033[31m'
BLUE = '\033[32m'

print(BLUE+"Bienvenido a tu identificador de numeros pares")

num = int(input(YELLOW+"Ingresa tu número: "))
res = num % 2

if res == 0 :
    print("Tu número es par")
else :
    print("Tu número es impar")
    