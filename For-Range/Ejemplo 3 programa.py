
def main2():
    f= int(input("Teclee f: "))

    suma = 0
    #Muestra y suma los valores desde 1 a f-1
    for valor in range (1, f):
        suma = suma + valor
        print(valor, end=" + ")
    #Muestra y suma el valor f
    suma +=f    
    print(f, " =",suma)
    
    
main2()

