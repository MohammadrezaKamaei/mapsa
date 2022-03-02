def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    matrix_T = []
    for j in range(columns):
        row = []
        for i in range(rows):
           row.append(matrix[i][j])
        matrix_T.append(row)

    return matrix_T


a=    ([[1, 4, 7],
       [2, 5, 8],
       [3, 6, 9]])

transpose_a = (transpose(a))

for r in transpose_a:
    print(r)