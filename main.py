import cv2
from sklearn import datasets

import arrays

# Indicaciones escritas en 30 segundos mientras brossard explicaba
# Promedio de todos los numeros, tipo ves todos
# los 5 en el datasest, y haces una nueva matrix con el promedio de todo los pixeles
# Mostrar los 10 promedios en la pantalla, mostrar una forma entendible,
# hacer que de 0 255 pase a 0 16, escala de grises pes
# Buscar los 3 dibujitos que se parecan mas, tipo dibujas un 6, quiza te salga 6, 8, 9
# Distancia euclediana, sacas ps, raiz cuadrada de , el primer pixel de tu numero - el primer pixel
# del otro numero + raiz cuadrada de tu numero nuevo - el 2do pixel del numero de arriba;
# 2 - 3 jueces tienen que estar de acuerdo

# Input
digits = datasets.load_digits()

# Números
numbers = arrays.new_matrix(10)

# Promedio de números
average_number = arrays.new_matrix(10)

# Constante de pixeles por dimensión
pixels = 8

for i in range(len(digits.target)):
    new_matrix = cv2.resize(digits.images[i], (pixels, pixels))
    numbers[digits.target[i]].append(new_matrix)


for i in range(len(average_number)):
    average_number[i] = arrays.matrix_mean(numbers[i], size=pixels)


# Aca cambias el numero de abajo, por ejemplo aca vez average_number[1], te dara el promedio del numero 1
# Lo cambias con los digitos del 0 al 9
for i in average_number[1]:
    print(i)
