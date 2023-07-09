from main import average_number
from colour import print_numbers_painting
# Impresion de las matrices de todos los numeros
for i in range(0, 10):
    print(f"La matriz promedio del numero {i} es: ")
    print("")
    # Recorremos toda la matriz y le aplicamos a cada numero la funcion para pintarlo
    for j in average_number[i]:
        for k in j:
            print_numbers_painting(k)
        print("")
    print("")

# @KarTaGo124

