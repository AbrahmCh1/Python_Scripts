

def paquete(costo):
    peso = 1
    costo = 0
    while peso != 0:
        peso = (int(input("Ingresa el peso de tu paquete en kg: ")))
        if peso > 0 and peso < 10:
            costo = costo + 1200
            print(f"Tu costo es de ${costo}")
        elif peso > 10 and peso < 45:
            costo = (costo+1200) + (peso*85) - 850
            print(f"Tu costo es de ${costo}")
        elif peso >= 45 and peso <= 90:
            costo = (costo+2700) + (peso*65) - 2925
            print(f"Tu costo es de ${costo}")
        elif peso > 90:
            costo = (costo + 3500) + (peso*75) - 6750
            print(f"Tu costo es de ${costo}")
    return (costo)


print("Bienvenido a tu sistema de paquetería")
paquete(0)
precio = paquete(costo)
print(f"Tu total es de {precio}")
