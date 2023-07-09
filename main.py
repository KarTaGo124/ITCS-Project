import cv2
from sklearn import datasets

import arrays


# Input
digits = datasets.load_digits()

# Números
numbers = arrays.new_matrix(10)

# Promedio de números
average_number = arrays.new_matrix(10)

# Constante de pixeles por dimensión
PIXELS = 8

for i in range(len(digits.target)):
    new_matrix = cv2.resize(digits.images[i], (PIXELS, PIXELS))
    numbers[digits.target[i]].append(new_matrix)


for i in range(len(average_number)):
    average_number[i] = arrays.matrix_mean(numbers[i], size=PIXELS)

