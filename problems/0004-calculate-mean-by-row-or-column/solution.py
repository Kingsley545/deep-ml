import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    rows, columns = len(matrix), len(matrix[0])
    
    means = [np.mean(row) for row in matrix] if mode == "row" else [np.mean(row) for row in np.transpose(matrix)]
    
    return means