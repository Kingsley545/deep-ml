import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
    cols_a = len(a[0])
    len_b = len(b)

    if cols_a != len_b:
        return -1
    
	return [np.dot(row, b) for row in a]