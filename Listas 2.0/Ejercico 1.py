# Práctica 1 - Juego de preguntas y respuestas

preguntas = ["¿El triángulo tiene 3 lados?", "La ballena es un animal mamifero",
             "¿Día de septiembre que se celebra la independencia de México?"]
respuestas = ["Verdadero", "Verdadero", 16]
puntos = 0

for i in range(len(preguntas)):
    print(preguntas[i])
    print(respuestas[i])

print("+ + + + QUE COMIENCE EL JUEGO + + + +")
input("- - <ENTER> para comenzar - -")

for i in range(len(preguntas)):
    print(f"Pregunta #{i+1} ", preguntas[i])
    respuesta = input("Respuesta: ").capitalize()

    if respuesta.isnumeric() == True:
        respuesta = int(respuesta)

    if respuesta == respuestas[i]:
        print("Respuesta correcta! :) ")
        puntos += 1

print("+ + + Fin del juego + + +")
