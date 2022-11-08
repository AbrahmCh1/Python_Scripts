#ACY 20/08/22
#propósito> Programa para dar el horóscopo
#Problema Tarea 3- Condicionales mútlpiles
#ITESM     

#codigo para ingresar rgb en la consola de python
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

print(colored(255,255,255, "****BIENVENID@ A TU HORÓSCOPO****"))
Sz = str(input(colored(153,255,255, "Ingresa tu signo zodiacal con letras minúsculas y sin acentos: ")))

if Sz == "cancer":
    print(colored(102,204,0,"Tendrás suerte este año"))
elif Sz == "virgo":
    print(colored(153,0,153,"Tendrás 'Harás fortuna'"))
elif Sz == "capricornio" :
    print(colored(0,128,255,"Viajarás mucho el próximo año"))
else :
    print(colored(255,128,0,"Tendrás mucha salud"))