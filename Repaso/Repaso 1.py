#ACY 02/09/22
#Programa dque muestra los productos en un while
#ITESM
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


print(colored(120,120,120,"***SISTEMA ALMACENES FABRICAS DE FRANCIA***"))
print("Esta es nuestra lista de precios")
print("\t A. Camisa $120")
print("\t B. Pantalón $250")
print("\t C. Jeans Casual $360")
print("\t X. Si ya no desea comprar")
producto=""
while(producto !="X"):
    producto = str(input("Ingresa la CLAVE del producto deseado: "))
    producto = producto.upper()
    if producto == "A":
        print("Camisa $120 agregada al carrito de compras")
        suma = suma +120
    elif producto =="B":
        print("Pantalón $250 agregado al carrito de compras")
        suma = suma +250
    elif producto == "C":
        print("Jeans Casual $360 agregado al carrito de compras")
        suma = suma +360
    else:
        if producto !="X":
            print("CLAVE NO VÁLIDA, produccto no agregado al carrito")
print(colored(147,25,120,f"\nTu total a pagar es ${suma}"))

