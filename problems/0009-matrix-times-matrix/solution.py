def dot(a:list[int|float], b:list[int|float])->int|float:
    return sum([first_val*second_val for first_val, second_val  in zip(a, b)])

def transpose(a: list[list[int|float]])-> list[list[int|float]]:
    rows, cols = len(a), len(a[0])
    out = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        for j in range(cols):
            out[i][j] = a[j][i]
    return out


def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    m1, n1 = len(a), len(a[0])
    m2, n2 = len(b), len(b[0])
    b_transpose = transpose(b)

    if n1 != m2:
        return -1
    result = [[0 for i in range(n2)] for j in range(m1)]
    for i in range(m1):
        for j in range(n2):
            result[i][j] = dot(a[i], b_transpose[j])
    
    return result