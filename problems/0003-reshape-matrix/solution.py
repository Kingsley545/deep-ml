import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    rows, cols = len(a), len(a[0])
    new_rows, new_cols = new_shape

    if rows * cols != new_rows * new_cols:
        return []
    a_array = np.array(a)
    reshaped_matrix = a_array.reshape(new_shape).tolist()

    return reshaped_matrix