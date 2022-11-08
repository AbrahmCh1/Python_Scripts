# ACY 02/09/22
# Programa de regresión
# ITESM

def main():
    try:
        n = int(input("Ingresa un número: "))
        for i in range(1, n+1):
            print(i, end=",")
        for i in range(n-1, 0, -1):
            if i != 1:
                print(i, end=",")
            else:
                print(i)
    except:
        print("Error")


main()
