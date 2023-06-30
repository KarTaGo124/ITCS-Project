from sklearn import datasets
import cv2
import pandas as pd



digits = datasets.load_digits()

# Promedio de todos los numeros, tipo ves todos
# los 5 en el datasest, y haces una nueva matrix con el promedio de todo los pixeles

# Mostrar los 10 promedios en la pantalla, mostrar una forma entendible,

# hacer que de 0 255 pase a 0 16, escala de grises pes

# Buscar los 3 dibujitos que se parecan mas, tipo dibujas un 6, quiza te salga 6, 8, 9

# Distancia euclediana, sacas ps, raiz cuadrada de , el primer pixel de tu numero - el primer pixel del otro numero + raiz cuadrada de tu numero nuevo - el 2do pixel del numero de arriba;

# 2 - 3 jueces tienen que estar de acuerdo


def matrices_mean(matrices):
    initial_matrix = [[0] * 8 for _ in range(8)]
    print(initial_matrix)
    for matrix in matrices:
        for i in range(8):
            for j in range(8):
                initial_matrix[i][j] += matrix[i][j]
    mean = [[initial_matrix[i][j] / len(initial_matrix) for j in range(8)] for i in range(8)]
    return mean


numbers = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: []}

average_number = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: []}

for i in range(len(digits.target)):
    new_matrix = cv2.resize(digits.images[i], (8, 8))
    numbers[digits.target[i]].append(new_matrix)

for i in range(len(average_number)):
    average_number[i] = matrices_mean(numbers[i])
