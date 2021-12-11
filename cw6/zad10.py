mat = [
    [6,1,1],
    [4,-2,5],
    [2,8,7],
]
def cross_depleted_matrix(matrix:list, row_ind:int, col_ind:int)->list:
    return [[matrix[row][col] for col in range(len(matrix[0])) if col != col_ind] for row in range(len(matrix)) if row != row_ind]

def determinant(matrix:list)->int:
    # row 1 col 1 expansion
    if len(matrix) == 1: return matrix[0][0]

    det = 0
    for i in range(len(matrix)):
        new_matrix = cross_depleted_matrix(matrix, i, 0)
        det += matrix[i][0] * (-1)**(((i+2)%2)) * determinant(new_matrix)
    return det

print(determinant(mat))