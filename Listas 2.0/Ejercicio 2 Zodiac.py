# Practice 2 / zodiac

# https://textkool.com/en/ascii-art-generator?hl=default&vl=default&font=ANSI%20Shadow&text=YOUR%20ZODIAC%20SIGN%0A
def printBanner():
    print("""
██╗   ██╗ ██████╗ ██╗   ██╗██████╗     ███████╗ ██████╗ ██████╗ ██╗ █████╗  ██████╗    ███████╗██╗ ██████╗ ███╗   ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗    ╚══███╔╝██╔═══██╗██╔══██╗██║██╔══██╗██╔════╝    ██╔════╝██║██╔════╝ ████╗  ██║
 ╚████╔╝ ██║   ██║██║   ██║██████╔╝      ███╔╝ ██║   ██║██║  ██║██║███████║██║         ███████╗██║██║  ███╗██╔██╗ ██║
  ╚██╔╝  ██║   ██║██║   ██║██╔══██╗     ███╔╝  ██║   ██║██║  ██║██║██╔══██║██║         ╚════██║██║██║   ██║██║╚██╗██║
   ██║   ╚██████╔╝╚██████╔╝██║  ██║    ███████╗╚██████╔╝██████╔╝██║██║  ██║╚██████╗    ███████║██║╚██████╔╝██║ ╚████║
   ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝""")


mes = ""
dia = 0
printBanner()
print("ADIVINARE TU SIGNO DEL ZODIACO")
print("Contesta así: 1 de Enero ó 20 de Julio")
fecha = str(input("¿Cuál es tu fecha de nacimiento? "))
lista = fecha.split(" ")
ubicacion = 0
for i in lista:
    if ubicacion == 0:
        dia = int(i)
    elif ubicacion == 2:
        mes = i
    ubicacion += 1

mes = mes.lower()
if (mes == "diciembre" and dia >= 22) or (mes == "enero" and dia <= 20):
    print("Tu signo es Capricornio ♑")
elif (mes == "enero" and dia >= 21) or (mes == "febrero" and dia <= 19):
    print("Tu signo zodiacal es Acuario ♒")
elif (mes == "febrero" and dia >= 20) or (mes == "marzo" and dia <= 20):
    print("Tu signo zodiacal es Piscis ♓")
elif (mes == "marzo" and dia >= 21) or (mes == "abril" and dia <= 20):
    print("Tu signo zodiacal es Aries ♈")
elif (mes == "abril" and dia >= 21) or (mes == "mayo" and dia <= 21):
    print("Tu signo zodiacal es Tauro ♉")
elif (mes == "mayo" and dia >= 22) or (mes == "junio" and dia <= 21):
    print("Tu signo zodiacal es Géminis ♊")
elif (mes == "junio" and dia >= 22) or (mes == "julio" and dia <= 23):
    print("Tu signo zodiacal es Cáncer ♋")
elif (mes == "julio" and dia >= 24) or (mes == "agosto" and dia <= 23):
    print("Tu signo zodiacal es Leo ♌")
elif (mes == "agosto" and dia >= 24) or (mes == "septiembre" and dia <= 23):
    print("Tu signo zodiacal es Virgo ♍")
elif (mes == "septiembre" and dia >= 24) or (mes == "octubre" and dia <= 23):
    print("Tu signo zodiacal es Libra ♎")
elif (mes == "octubre" and dia >= 24) or (mes == "noviembre" and dia <= 22):
    print("Tu signo zodiacal es Escorpio ♏")
elif (mes == "noviembre" and dia >= 23) or (mes == "diciembre" and dia <= 21):
    print("Tu signo zodiacal es Sagitario ♐")
else:
    print("No es una fecha válida")
