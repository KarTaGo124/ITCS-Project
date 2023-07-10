def euclidean_distance(array1: list, array2: list):
    """
    Calculate distances with Euclidean formula.
    @OcZi
    :param array1: first array to compare.
    :param array2: second array to compare.
    :return: total distance of all arrays.
    """
    summ = 0
    for index in range(0, len(array1)):
        summ += (array1[index] - array2[index]) ** 2
    return int(summ ** 0.5)

