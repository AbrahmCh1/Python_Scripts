# ACY 09/09/22
# propósito> Programa para calcular el promedio de calificaciones
# Problema Exámen 2
# ITESM

# define la función promedio
def promedio():
    calificacion = 0
    try:  # Revisa para tipo de datos no válidos
        for i in range(3):
            calificacion += float(
                input(f"Dame la calificación {i+1}: "))
        nueva_calificacion = calificacion/3
        print(f"El promedio de las 3 calificaciones es: {nueva_calificacion}")
    except:
        print("Tipo de dato no válido")


promedio()  # Llama a la función
