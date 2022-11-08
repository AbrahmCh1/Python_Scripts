#Ejercicio 3 for con range 30/08/2022 ACY
from gtts import gTTS
from playsound import playsound

mensaje = str(input("¿Cuál es el mensaje a transmitir? "))

for letra in mensaje:
    print(f"Se transmitió la letra {letra}")
audio=gTTS(mensaje)
audio.save("Mi_mensaje.mp3")
playsound("Mi_mensaje.mp3")
