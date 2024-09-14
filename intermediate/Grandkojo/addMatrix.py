#!/usr/bin/python3

from typing import List

def addMatrices(firstMatrix: List[List[int]], secondMatrix: List[List[int]]) -> None:
    """ adds two matrices together
    """
    # check if matrix is empty
    if not firstMatrix or  not firstMatrix[0]:
        return  "First matrix is empty"
    if not secondMatrix or not secondMatrix[0]:
        return "Second matrix is empty"
    
    
    first_matr_row = len(firstMatrix)
    first_matr_col = len(firstMatrix[0])
    second_matr_row = len(secondMatrix)
    second_matr_col = len(secondMatrix[0])

    if first_matr_col != second_matr_col:
        return "Matrices to add must have the same number of columns"
    if first_matr_row !=second_matr_row:
        return "Matrices to add must have the same number of rows"
    
    result_matrix = []
    for row in range(first_matr_row):
        result_row = []

        for col in range(first_matr_col):
            sum_elements = firstMatrix[row][col] + secondMatrix[row][col]
            result_row.append(sum_elements)
        result_matrix.append(result_row)
    return result_matrix


def print_matrix(matrix):
    print(matrix)
    for row in matrix:
        print(" ".join(map(str, row)))
    

# Example usage
matrix_2x2_1 = [
    [1, 2],
    [3, 4]
]

matrix_2x2_2 = [
    [1, 2],
    [4, 5]
]

print_matrix(addMatrices(matrix_2x2_1, matrix_2x2_2))
# print_matrix(addMatrices(matrix_2x2_1, matrix_2x2_2))