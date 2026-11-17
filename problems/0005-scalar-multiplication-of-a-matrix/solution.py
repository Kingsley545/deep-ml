import numpy as np

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    # Your code here
    rows, cols = len(matrix), len(matrix[0])
    reshaped_matrix = np.array(matrix).reshape(-1)
    output = reshaped_matrix * scalar
    output = output
    return output.reshape(rows, cols).tolist()