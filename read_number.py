import cv2
from colour import print_numbers_painting
from main import image

print(f"La matriz del número leído es: ")
print("")
# Recorremos toda la matriz y le aplicamos a cada numero la funcion para pintarlo
for i in image:
    for j in i:
        print_numbers_painting(j)
    print("")



