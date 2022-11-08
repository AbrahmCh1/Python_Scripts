#ACY 23/08/2022
#Ejemplo de una función definida por el usuario pasando parametros
#Programa que sirve para restar 2 numero inicializados por el usuario
#ITESM
#codigo para ingresar rgb en la consola de python
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def resta(x,y):
    input(colored(142,255,18, f"Entraste a la función de resta, presiona la tecla ENTER para mostrar el resultado de {a} - {b}"))
    print(colored(117,117,117, "El resultado de la resta es"), a-b)

print("****INICIO DEL PROGRAMA DE RESTA****")
a= int(input(colored(127, 184, 255, "Ingresa tu primer número: ")))
b= int(input(colored(127, 184, 255, "Ingresa tu segundo número: ")))
resta(a,b)#Invocamos la función resta
print(colored(255,255,255, "\nFin del programa"))