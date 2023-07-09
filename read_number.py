import cv2
from colour import print_numbers_painting
# Usamos cv2.imread para leer la imagen en escala de grises
img_array = cv2.imread("ejemplo.png", cv2.IMREAD_GRAYSCALE)
# Usamos cv2.resize para cambiar el tamaño de la imagen a 8x8
nueva_img = cv2.resize(img_array, (8,8))

# Recorremos toda la imagen con la finalidad de
# poder cambiar a cada elemento al rango de 0 a 16

for i in range(8):
    for j in range(8):
        nueva_img[i][j] = 255 - nueva_img[i][j]

for i in range(8):
    for j in range(8):
        nueva_img[i][j] = nueva_img[i][j]*16/255

print(f"La matriz del número leído es: ")
print("")
# Recorremos toda la matriz y le aplicamos a cada numero la funcion para pintarlo
for i in nueva_img:
    for j in i:
        print_numbers_painting(j)
    print("")



