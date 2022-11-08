#ACY 23/08/2022
#Ejemplo de una función definida por el usuario- sin paso de parametros
#Programa que sirve para sumar 2 numero inicializados por el usuario
#ITESM
#codigo para ingresar rgb en la consola de python
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
a=1 #INICIALIZAR
b=6

def suma(): #Creamos la función suma
    input(colored(255,100,255,f"Entraste a la función de suma, presiona una tecla para mostrar el resultado de {a} + {b}"))
    print(colored(120, 145, 255, "El resultado de la suma es"), a+b)

print("****INICIO DEL PROGRAMA****")
suma()#Invocamos la función suma
print("\nFin del programa")
#FIN