import cv2
from colored import Fore
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


def digit_by_index(i: int):
    return digits.target[i]


def read_number_image():
    # Usamos cv2.imread para leer la imagen en escala de grises
    img_array = cv2.imread("ejemplo.png", cv2.IMREAD_GRAYSCALE)
    # Usamos cv2.resize para cambiar el tamaño de la imagen a 8x8
    nueva_img = cv2.resize(img_array, (8, 8))

    # Recorremos toda la imagen con la finalidad de
    # poder cambiar a cada elemento al rango de 0 a 16
    for y in range(8):
        for x in range(8):
            nueva_img[y][x] = (255 - nueva_img[y][x]) * 16 / 255
    return nueva_img


image = read_number_image()

def same_elements(array) -> bool:
    first = array[0]
    for elem in range(1, len(array)):
        if elem != first:
            return False
    return True

def print_ai(*array):
    colours = Fore.RGB(124, 252, 0)
    print(f"{colours}Hola, ¡soy la inteligencia artificial!")

    if len(array) < 2 or same_elements(array):
        print(f"{colours}He detectado que el digito es el número {array[0]}!")
    else:
        print(f"{colours}He detectado que el digito se parece a los números:")
        print(array)

    print(f"{colours}¿Estás satisfecho con el resultado?")
    answer = input(":").lower()
    if answer == "si":
        print(f"{colours}Muchas gracias :)")
    else:
        print(f"{colours}Lo siento :(")
        answer = input(":").lower()
        if answer == "no digas eso papu":
            print(f"{colours}Tienes razón, pronto mejoraré :)")