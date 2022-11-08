nombre = str.lower(input("Escribe tu nombre completo: "))
lets = str.lower(input("Letra a no enmascarar: "))
c = 0


for letra in nombre:
    if letra == " ":
        print("   ", end="")
    elif letra != lets:
        print("*", end="")
    else:
        print(lets, end="")
