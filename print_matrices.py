import main


def imprimir_numeros_coloreados(numeros):
    for numero in numeros:
        if numero == 0:
            # Imprimir número 0 en color negro
            print(" " + "\033[30m{}\033[0m".format(numero), end=" ")
        elif numero == 16:
            # Imprimir número 16 en color blanco
            print("\033[97m{}\033[0m".format(numero), end=" ")
        else:
            # Calcular el valor de escala entre blanco y negro
            escala = int(232 + (23 * (numero - 1) / 15))

            # Imprimir números del 1 al 15 con colores intermedios
            # Correcciones en estetica al imprimir la matriz
            if len(str(numero)) == 1:
                print(" " + "\033[38;5;{}m{}\033[0m".format(escala, numero), end=" ")
            else:
                print("\033[38;5;{}m{}\033[0m".format(escala, numero), end=" ")


# imprimir la matriz de forma entendible
def imprimir_matriz_8x8(matriz):
    for fila in matriz:
        imprimir_numeros_coloreados(fila)
        print("")


# Impresion de las matrices de todos los numeros
for i in range(0, 10):
    print(f"La matriz promedio del numero {i} es: ")
    print("")
    imprimir_matriz_8x8(main.average_number[i])
    print("")


