#Ejercicio 3 for con range 30/08/2022 ACY
from gtts import gTTS
from playsound import playsound
from subprocess import call

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


##HACERLO CON FUNCION DE LETRAS
mensaje = str(input("¿Cuál es el mensaje a transmitir? "))

for letra in mensaje:
    print(colored(255,128,0,f"Se transmitió la letra {letra}"))
audio=gTTS(mensaje)
audio.save("perro.mp3")
call(["afplay","perro.mp3"])