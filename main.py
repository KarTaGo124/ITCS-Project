from sklearn import datasets
import cv2


# Indicaciones escritas en 30 segundos mientras brossard explicaba
# Promedio de todos los numeros, tipo ves todos
# los 5 en el datasest, y haces una nueva matrix con el promedio de todo los pixeles
# Mostrar los 10 promedios en la pantalla, mostrar una forma entendible,
# hacer que de 0 255 pase a 0 16, escala de grises pes
# Buscar los 3 dibujitos que se parecan mas, tipo dibujas un 6, quiza te salga 6, 8, 9
# Distancia euclediana, sacas ps, raiz cuadrada de , el primer pixel de tu numero - el primer pixel
# del otro numero + raiz cuadrada de tu numero nuevo - el 2do pixel del numero de arriba;
# 2 - 3 jueces tienen que estar de acuerdo

digits = datasets.load_digits()


# Promedio de la matriz
def matrices_mean(matrices):
    initial_matrix = [[0] * 8 for _ in range(8)]
    for matrix in matrices:
        for i in range(8):
            for j in range(8):
                initial_matrix[i][j] += matrix[i][j]
    mean = [[round(initial_matrix[i][j] / len(matrices), 2) for j in range(8)] for i in range(8)]
    return mean


# Diccionario para almacenar los numeros
numbers = [[], [], [], [], [], [], [],  [], [], []]

for i in range(len(digits.target)):
    new_matrix = cv2.resize(digits.images[i], (8, 8))
    numbers[digits.target[i]].append(new_matrix)

# Diccionario para almacenar los numeros promedios
average_number = [[], [], [], [], [], [], [],  [], [], []]

for i in range(len(average_number)):
    average_number[i] = matrices_mean(numbers[i])

for i in average_number[0]:
    print(i)
