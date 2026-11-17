import numpy as np

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = matrix[i][j] * scalar

    return matrix