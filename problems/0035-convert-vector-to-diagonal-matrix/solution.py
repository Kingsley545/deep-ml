import numpy as np

def make_diagonal(x):
	# Your code here
    n = len(x)
    out = [[0 for i in range(n)] for i in range(n)]

    for i in range(n):
        out[i][i] = x[i]

    return out