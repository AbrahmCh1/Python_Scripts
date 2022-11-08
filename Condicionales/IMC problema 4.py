#ACY 19/08/22
#propósito> Programa para calcular el IMC
#Problema 4- Condicionales
#ITESM
YELLOW = '\033[33m'
BLUE = '\033[32m'

print(BLUE+"****BIENVENIDO A TU CALCULADORA DE TU IMC****")
try: 
    peso = float(input(YELLOW+"Ingresa tu peso en kilogramos:"))
    altura = float(input("Ingresa tu altura en metros:"))

    IMC = peso / (altura**2)
    print(f"tuviste un IMC de {IMC:.0f}")
    if IMC < 20 :
        print("Peso bajo")
    elif IMC >= 20 and IMC <25 :
        print("Peso normal")
    elif IMC >= 25 and IMC <30 :
        print("Sobrepeso")
    elif IMC >= 30 and IMC <40 :
        print("Obesidad")
    else: 
        print("Ingresaste datos de peso y/o altura invalidos")

except:
    print("Error de tipo de dato, contacta al administrador del sistema")