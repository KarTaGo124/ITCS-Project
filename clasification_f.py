import cv2

import arrays
import main

for index, digit in enumerate(main.digits.data):
    matrix = cv2.resize(digit, (main.PIXELS, main.PIXELS))
    matrix = arrays.matrix_mean(matrix, size=main.PIXELS)
    print("index", index, matrix)













