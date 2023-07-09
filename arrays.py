

def new_matrix(size, fill_value=None):
    """
    Create a new simple matrix.
    @OcZi
    :param size: size of 2nd dimension.
    :param fill_value: value to fill 2nd dimension.
    :return: matrix of empty (or filled) arrays.
    """
    arr = []
    for _ in range(size):
        sub = []
        if fill_value is not None:
            sub.append(fill_value)
        arr.append(sub)
    return arr


def matrix_mean(matrices, size: int = 8):
    """
    Mean of matrices.
    @Falaxsa
    :param matrices: matrices to calculate mean.
    :param size: size of array output.
    :return: array mean of matrices.
    """
    initial_matrix = [[0] * size for _ in range(size)]
    for matrix in matrices:
        for i in range(size):
            for j in range(size):
                initial_matrix[i][j] += matrix[i][j]

    matrices_size = len(matrices)
    mean = [[int(round(initial_matrix[i][j] / matrices_size)) for j in range(size)] for i in range(size)]

    return mean

