

def euclidean_distance(*dimensions: int):
    """
    Calculate distances with Euclidean formula.
    Example:
        # Parameters needs to be length-pair!
        euclidean_distance(
            10, 20, # X axis distance: 10
            5, 10 # Y axis distance: 5
        )
    :param dimensions: dimensions to calculate (4 elements -> 2 dimensions of 2 sets)
    :return: distance of 2 sets.
    """
    if len(dimensions) % 2 != 0:
        raise ValueError(f"Dimension length should be pair! (length: {len(dimensions)})")
    summ = 0

    for index in range(0, len(dimensions), 2):
        summ += (dimensions[index] - dimensions[index + 1]) ** 2
    return int(summ ** 0.5)
