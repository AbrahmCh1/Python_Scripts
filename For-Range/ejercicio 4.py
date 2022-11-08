#Ejercicio 4 for con range 30/08/2022 ACY
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


Perros = ["Bulldog","Chihuahua","Pug","Pastor alemán","Mestizo"]
for x in Perros:
    print("Raza: " + x)
    if x =="Chihuahua":
        print(colored(255,0,0,"\t¡Me encanta esa raza de perro!\n"))