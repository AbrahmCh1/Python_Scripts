def main():
    num= int(input("Ingresa el número del que deseas obtener su tabla de multiplicación: "))
    for i in range(1,10):
        if num !=0:
            print(f"La multiplicación de {num} * {i} = {num*i} ")
        else:
            print("Debes ingresar un número mayor a 0")
            break

print("Bienvenido al programa para tu tabla de multiplicar")
main()