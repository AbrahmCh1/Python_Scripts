respuestas = [
    ['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D']
    ["D", "B", "A", "B", "C", "A", "E", "E", "A", "D"]
    ["E", "D", "D", "A", "C", "B", "E", "E", "A", "D"]
    ["C", "B", "A", "E", "D", "C", "E", "E", "A", "D"]
    ["A", "B", "D", "C", "C", "D", "E", "E", "A", "D"]
    ["B", "B", "E", "C", "C", "D", "E", "E", "A", "D"]
    ["B", "B", "A", "C", "C", "D", "E", "E", "A", "D"]
    ["E", "B", "E", "C", "C", "D", "E", "E", "A", "D"]]

llave = ["D", "B", "D", "C", "C", "D", "A", "E", "A", "D"]

for i in range(len(respuestas)):
    correctas = 0
    for j in range(len(respuestas[i])):
        if respuestas[i][j] == llave[j]:
            correctas += 1

    print(f"Alumno {i} tuvo {correctas} respuestas correctas")
