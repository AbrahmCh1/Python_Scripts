# ACY 09/09/22
# propósito> Programa para calcular el costo por paquete
# Problema Exámen 1
# ITESM

costo = 0
peso = 1

print("**** Bienvenido a DHL Express****\n")
print("Peso", end="\t\t")
print("\tCosto\n")
print("___________________________________________")
print("Entre 1 y 10 kg ---- Tarifa fija de $120")
print("Más de 10 kg    ---- Tarifa fija de $270\n")
print("\t PRESIONA 0 para terminar\n")
try:
    while peso > 0:  # Mientras que el peso sea mayor a 0
        peso = int(input("Proporcione el peso de su paquete en kg: "))
        if peso >= 1 and peso <= 10:  # Si el peso sea igual o mayor a 1 y menor a 10
            print("\t Entre 1 y 10 kg ---- Tarifa fija de $120\n")
            costo += 120
        elif peso > 10:  # Si el peso es igual o mayor a 10
            print("\t Más de 10 kg    ---- Tarifa fija de $270\n")
            costo += 270
        else:  # Si el costo es 0
            print(f"\n   El total de costos de envío es: ${costo}")
except:
    print("Tipo de dato no válido")
# FIN
