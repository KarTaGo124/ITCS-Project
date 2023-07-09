import main

from colored import Back


def imprimir_numeros_coloreados(numeros):
    for numero in numeros:
        if numero == 0:
            # Imprimir número 0 en color negro
            print(Back.RGB(0, 0, 0) + " " + str(numero), end=" ")
        elif numero == 16:
            # Imprimir número 16 en color blanco

            print(Back.RGB(255, 255, 255) + " " + str(numero), end=" ")
        else:
            # Calcular el valor de escala entre blanco y negro
            escala = int((16 * numero) - 1)

            # Imprimir números del 1 al 15 con colores intermedios
            # Correcciones en estetica al imprimir la matriz
            if len(str(numero)) == 1:
                print(Back.RGB(escala, escala, escala) + " " + str(numero), end=" ")
            else:
                print(Back.RGB(escala, escala, escala) + str(numero), end=" ")


# imprimir la matriz de forma entendible
def imprimir_matriz_8x8(matriz):
    for fila in matriz:
        imprimir_numeros_coloreados(fila)
        # Rompe el color blanco aquí
        print(Back.RGB(0, 0, 0) + " ")


# Impresion de las matrices de todos los numeros
for i in range(0, 10):
    print(f"La matriz promedio del numero {i} es: ")
    print("")
    imprimir_matriz_8x8(main.average_number[i])
    print("")
