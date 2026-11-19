import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    trace = a + d
    det = (a * d) - (b * c)
    eigenvalues = sorted([(np.sqrt(trace ** 2 - (4 * det)) + trace) / 2, (trace - np.sqrt(trace ** 2 - (4 * det))) / 2], reverse=True)
    
    return eigenvalues