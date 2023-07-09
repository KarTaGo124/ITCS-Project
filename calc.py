def euclidean_distance(array1: list, array2: list):
    """
    Calculate distances with Euclidean formula.
    Example:
        # Parameters needs to be length-pair!
        euclidean_distance(
            10, 20, # X axis distance: 10
            5, 10 # Y axis distance: 5
        )
    :param array1: array2 to calculate (4 elements -> 2 dimensions of 2 sets)
    :return: distance of 2 sets.
    """
    summ = 0
    for index in range(0, len(array1)):
        summ += (array1[index] - array2[index]) ** 2
    return int(summ ** 0.5)
