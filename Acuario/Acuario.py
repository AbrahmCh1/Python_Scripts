# Programa Sistema Acuario Aqua
# Práctica Final - archivos de texto e imágenes
# ACY
# ITESM
from datetime import datetime
from tqdm import tqdm  # Se debe instalar
from time import sleep
from PIL import Image
archivo = open("registro_acuario.txt", "a")

# codigos colores
RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
BLUE = '\033[34m'
RESET = '\033[0m'


def calculo_total(dulce, salada):
    return (dulce * 200 + salada * 500)


print(RESET)
print("\033[4;33;44m * * * * * Bienvenido al Sistema Acuario Aqua  * * * * \033[0;m \n")
#  4   subrayado/33 color letra amarilla /44 fondo azul / m cierre del color  /  \033[0;m  resetea color
now = datetime.now()
print(" Hoy estamos a", now)
print("")

print(" - - - Catálogo de peces - - -")
print("\t Agua dulce $200 c/u")
print("\t Agua salada $500 c/u")
print("")

cliente = str(input("Nombre del cliente: "))
p_dulce = int(input("¿Cuántos peces de agua dulce deseas comprar? "))
p_salada = int(input("¿Cuántos peces de agua salada deseas comprar? "))

print("Tu total a pagar es: $", calculo_total(p_dulce, p_salada))
print("")
# Comenzamos a guardar datos en archivo de texto
archivo.write("\n*** Acuario Aqua ***")
archivo.write("\nFecha: " + str(now))
archivo.write("\n Nombre cliente: " + cliente)
archivo.write("\n ----Detales de la compra ---- ")
archivo.write("\n Peces de agua dulce: " + str(p_dulce) + " a $200 c/u")
archivo.write("\n Peces de agua salada: " + str(p_salada) + " a $500 c/u")
archivo.write("\n Total pagado: $" + str(calculo_total(p_dulce, p_salada)))

if calculo_total(p_dulce, p_salada) > 1500:
    print("\033[3;33;45m Felicidades! Ganaste un premio, ¿Cuál quieres? \033[0;m")
    print("\t Opción 1: Un pez extra de agua dulce")
    print("\t Opción 2: Alimento vivo")
    print("\t Opción 3: Limpieza de la pecera gratis!")
    print("")
    opcion = int(input("Elige una opción [1] [2] [3]: "))
    if opcion == 1:
        print("Elegiste - Un pez extra de agua dulce! ")
        I1 = Image.open("pez.jpg")
        I1.show()
        archivo.write("\nPremio- Pez de agua dulce")
    elif opcion == 2:
        print("Elegiste - Alimento vivo! ")
        I1 = Image.open("artemia.jpg")
        I1.show()
        archivo.write("\nPremio- Alimento vivo")
    elif opcion == 3:
        print("Elegiste - Limpieza de la pecera gratis!")
        I1 = Image.open("limpieza.jpg")
        I1.show()
        archivo.write("\nPremio- Limpieza de la pecera gratis")
    else:
        print("Opción no válida! Lo siento")
else:
    print("Premio: No se alcanzó monto mínimo de compra para la promoción")
    archivo.write(
        "\nNo se alcanzó monto mínimo de compra para llevarse premio")

for i in tqdm(range(100), desc="Guardando en archivo. Espere..."):
    sleep(0.01)
print("Datos guardados con éxito!")


print("\n * * * ESTAS SON LAS TODAS VENTAS A LA FECHA * * * * ")
archivo = open("registro_acuario.txt", "r")
cont = archivo.read()
print(cont)
