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
    img_array = cv2.imread("image.png", cv2.IMREAD_GRAYSCALE)
    # Usamos cv2.resize para cambiar el tamaño de la imagen a 8x8
    nueva_img = cv2.resize(img_array, (8, 8))

    # Recorremos toda la imagen con la finalidad de
    # poder cambiar a cada elemento al rango de 0 a 16
    for y in range(8):
        for x in range(8):
            nueva_img[y][x] = (255 - nueva_img[y][x]) * 16 / 255
    return nueva_img


def print_ai(array, mean: bool = False):
    colours = Fore.RGB(124, 252, 0)
    print(f"{colours}Hola, ¡soy la inteligencia artificial!")

    if mean:
        print(f"{colours}He detectado que el digito es el número {array[0]}!")
    else:
        if array[0] == array[1] == array[2]:
            print(f"{colours}He detectado que el digito es el número {array[0]}:")
        elif (best := elem_matches(array[:3])) != -1:
            print(f"{colours}He detectado que el digito se parece al número {best}:")
        else:
            #     : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
            freq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            cnt = 0
            while 5 not in freq:
                number = array[cnt]
                freq[number] += 1
                cnt += 1

            print(f"{colours}Y despues de llamar a {cnt} jueces")
            print(f"{colours}Doy el veredicto que el digito se parece al numero {freq.index(5)}")

    print(f"{colours}¿Estás satisfecho con el resultado?")
    answer = input(":").lower()
    if answer == "si":
        print(f"{colours}Muchas gracias :)")
    else:
        print(f"{colours}Lo siento :(")
        answer = input(":").lower()
        if answer == "no digas eso papu":
            print(f"{colours}Tienes razón, pronto mejoraré :)")


image = read_number_image()


def elem_matches(array):
    """
    Get the number with most matches or -1
    :param array: array of numbers
    :return: get number with most matches (or -1)
    """
    matches = {}
    for index in range(len(array)):
        elem1 = array[index]
        for j, elem2 in enumerate(array):
            if index == j:
                continue

            if elem1 == elem2:
                if elem1 not in matches:
                    matches[elem1] = 1
                else:
                    matches[elem1] += 1

    best = -1
    repeated = -1
    for num, repeats in matches.items():
        if repeats > 1 and repeats > repeated:
            best = num
            repeated = repeats

    return best
