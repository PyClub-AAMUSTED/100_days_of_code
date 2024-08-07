import unittest

from ..addMatrix import addMatrices, print_matrix

class TestAddMatrix(unittest.TestCase):
    
    def test_matrices_different_rows(self):
        matrix_1 = [[1, 2], [3, 4]]
        matrix_2 = [[1, 2], [4, 5], [4, 9]]
        self.assertEqual(addMatrices(matrix_1, matrix_2), "Matrices to add must have the same number of rows")
    
    def test_second_matrix_empty(self):
        matrix_1 = [[1, 2], [3, 4]]
        self.assertEqual(addMatrices(matrix_1, None), "Second matrix is empty")
    
    def test_first_matrix_empty(self):
        matrix_2 = [[1, 2], [4, 5], [4, 9]]
        self.assertEqual(addMatrices(None, matrix_2), "First matrix is empty")
    
    def test_matrices_different_columns(self):
        matrix_1 = [[1, 2], [3, 4]]
        matrix_2 = [[1, 2, 5], [4, 5], [4, 9]]
        self.assertEqual(addMatrices(matrix_1, matrix_2), "Matrices to add must have the same number of columns")
    
    def test_valid_matrix_addition(self):
        matrix_1 = [[1, 2], [3, 4]]
        matrix_2 = [[5, 6], [7, 8]]
        expected_result = [[6, 8], [10, 12]]
        self.assertEqual(addMatrices(matrix_1, matrix_2), expected_result)

    def test_both_matrices_empty(self):
        matrix_1 = []
        matrix_2 = []
        self.assertEqual(addMatrices(matrix_1, matrix_2), "First matrix is empty")

    def test_single_element_matrices(self):
        matrix_1 = [[1]]
        matrix_2 = [[2]]
        expected_result = [[3]]
        self.assertEqual(addMatrices(matrix_1, matrix_2), expected_result)

    def test_negative_values(self):
        matrix_1 = [[-1, -2], [-3, -4]]
        matrix_2 = [[1, 2], [3, 4]]
        expected_result = [[0, 0], [0, 0]]
        self.assertEqual(addMatrices(matrix_1, matrix_2), expected_result)

    def test_non_integer_values(self):
        matrix_1 = [[1.5, 2.5], [3.5, 4.5]]
        matrix_2 = [[0.5, 1.5], [2.5, 3.5]]
        expected_result = [[2.0, 4.0], [6.0, 8.0]]
        self.assertEqual(addMatrices(matrix_1, matrix_2), expected_result)

    def test_large_matrices(self):
        matrix_1 = [[1] * 1000] * 1000
        matrix_2 = [[2] * 1000] * 1000
        expected_result = [[3] * 1000] * 1000
        self.assertEqual(addMatrices(matrix_1, matrix_2), expected_result)

if __name__ == '__main__':
    unittest.main()