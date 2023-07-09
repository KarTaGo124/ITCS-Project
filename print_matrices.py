import main
def imprimir_numeros_coloreados(numeros):
    for numero in numeros:
        if numero == 0:
            # Imprimir número 0 en color negro
            print(" "+"\033[30m{}\033[0m".format(numero), end=" ")
        elif numero == 16:
            # Imprimir número 16 en color blanco
            print("\033[97m{}\033[0m".format(numero), end=" ")
        else:
            # Calcular el valor de escala entre blanco y negro
            escala = int(232 + (23 * (numero - 1) / 15))
            # Imprimir números del 1 al 15 con colores intermedios
            ####################
            # Las siguientes condicionales son debido a que al momento de imprimir la matriz
            # los numeros no se acomodaban bien debido a que algunos tienen 1 cifra y otros 2
            if len(str(numero)) == 1:
                print(" "+"\033[38;5;{}m{}\033[0m".format(escala, numero), end=" ")
            else:
                print("\033[38;5;{}m{}\033[0m".format(escala, numero), end=" ")


# imprimir_matriz_8x8 usa la lista de listas 8x8 para imprimir la matriz de forma que pueda
# ser entedible para el ser humano
def imprimir_matriz_8x8(matriz):
    for fila in matriz:
        imprimir_numeros_coloreados(fila)
        print("")
# Uso un for para recorrer numeros del rango de 0 a 9 asi imprimiendo cada una de las matrices respectivas
for i in range(0,10):
    print(f"La matriz promedio del numero {i} es: ")
    print("")
    imprimir_matriz_8x8(main.average_number[i])
    print("")