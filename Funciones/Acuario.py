#ACY 23/08/2022
#Programa para calcular el total de precio de un acuario
#ITESM
from datetime import datetime
def calculo_total(dulce,salado): 
    dulce = dulce * 200
    salado = salado * 500
    return(dulce + salado)

print("*********Bienvenido al programa*********") 
date = datetime.now() 
print(date)
print("\n¿Cuántos peces comprarás?") 
p_dulce = int(input("Agua dulce $200 c/u: "))
p_salado = int(input("Agua salada $500 c/u: "))
ct = calculo_total(p_dulce, p_salado) 
print("Peces de agua dulce: ", p_dulce, " $", p_dulce*200)
print("Peces de agua salada: ", p_salado, "$", p_salado*500)
print("Precio Total es de: $",ct)
if ct > 1500: 
        print("\n¡Felicidades! tu cuenta es mayor de $1500")
        print("Selecciona un premio:")
        print("Un pez de agua dulce extra [1]")
        print("Alimento vivo! [2]")
        print("Limpieza de pecera gratis! [3]")
        pr = int(input()) 
        if pr == 1:
            print("Has ganado un pez de agua dulce") 
        elif pr == 2:
            print("Has ganado alimento vivo!")
        elif pr == 3:
            print("Has ganado una limpieza de pecera gratis")
        else:
            print ("Opción Inválida")
else:
    print("No has ganado ningún premio") 



