import main
from main import image, digits
import calc


image_array = []
distances = []
values_distance = []

# Matrix to array
for i in image:
    for j in i:
        image_array.append(j)

for i in range(len(digits.data)):

    value = calc.euclidean_distance(image_array, digits.data[i])
    values_distance.append((value, digits.target[i]))

values_distance = sorted(values_distance)

# Judges
first, second, third = values_distance[0][1], values_distance[1][1], values_distance[2][1]

print(f"Los jueces dicen que los target mas cercanos al digito ingresado son: {first}, {second}, {third}")

targets = [values_distance[i][1] for i in range(len(values_distance))]

main.print_ai(targets)









