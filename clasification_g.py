import calc
import main


# Target
# Key value:
# "digit":euclidean_distance output here
# FIXME: less distance == more probability??
# Example:
# {
# "1":20,
# "2":30
# "4":5
# }


def dict_sorted_digits(to_compare: dict[str, list]):
    ordered_list = sorted(to_compare.items(), key=lambda item: item[1])

    digits = {}
    for item in ordered_list:
        digits[item[0]] = item[1]
    return digits


def calculate_distances(image_array, to_compare: dict[str, list]):
    targets = {}
    for digit, array_digit in to_compare.items():
        for x in range(8):
            processed = calc.euclidean_distance(image_array[x], array_digit[x])
            if digit not in targets:
                targets[digit] = processed
            else:
                targets[digit] += processed
    return targets


# G)

# Average linked to his digit
average_index = {main.digit_by_index(i): main.average_number[i] for i in range(len(main.average_number))}

# Calculate distances of image to each digit
distances = calculate_distances(main.image, average_index)

# Ordered distances
ordered = dict_sorted_digits(distances)

# Accessing by key index
keys = list(ordered.keys())

main.print_ai(keys, mean=True)
