def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0],  matrix[1][1]
    result = [[0 for i in range(2)] for j in range(2)]
    det = (a * d) - (b * c)
    if det == 0:
        return None
    for i in range(2):
        for j in range(2):
            if i == j:
                result[i][j] = d/det if i == 0 else a/det
            else:
                result[i][j] = (-b/det) if i == 0 else (-c/det)
    return result