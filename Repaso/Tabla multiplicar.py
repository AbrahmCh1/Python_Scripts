
def tabla_multiplicar():
    n=int(input("Ingresa el número de la tabla de multiplicar que deseas: "))
    for i in range(1,11):
        if n == 0: 
            print("No se puede hacer la tabla de multiplicar de 0")
            break
        else:
            print(f"{n} x {i} = {n*i}")
    

#Llamar a la función
tabla_multiplicar()

