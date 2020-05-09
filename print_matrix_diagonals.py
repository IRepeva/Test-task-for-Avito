import numpy as np
import unittest


class MatrixTest(unittest.TestCase):
    def test_empty(self):
        array = []

        self.assertEqual(diagonals_print_v1(array), [])
        self.assertEqual(diagonals_print_v2(array), [])
        self.assertEqual(diagonals_print_v3(array), [])
        self.assertEqual(diagonals_print_v4(array), [])

    def test_matrix(self):
        array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = [[1], [2, 4], [3, 5, 7], [6, 8], [9]]

        self.assertEqual(diagonals_print_v1(array), result)
        self.assertEqual(diagonals_print_v2(array), result)
        self.assertEqual(diagonals_print_v3(array), result)
        self.assertEqual(diagonals_print_v4(array), result)

    def test_square(self):
        array = [[1, 2, 3], [4, 5, 6]]

        with self.assertRaises(AssertionError):
            diagonals_print_v1(array)
            diagonals_print_v2(array)
            diagonals_print_v3(array)
            diagonals_print_v4(array)

    def test_single(self):
        array = [1]

        self.assertEqual(diagonals_print_v1(array), array)
        self.assertEqual(diagonals_print_v2(array), array)
        self.assertEqual(diagonals_print_v3(array), array)
        self.assertEqual(diagonals_print_v4(array), array)



def diagonals_print_v1(matrix):
    size = len(matrix)
    array = np.array(matrix)
    try:
        assert size == len(matrix[0]), "Please use square matrix"
        matrix = np.array(array)[:, ::-1]
        diagonals = [matrix.diagonal(i) for i in range(size - 1, -size, -1)]
        return [n.tolist() for n in diagonals]
    except (IndexError, TypeError):
        return matrix


def diagonals_print_v2(matrix):
    size = len(matrix)
    if size > 1:
        assert size == len(matrix[0]), "Please use square matrix"
        diagonals = [[] for _ in range(2 * size - 1)]

        for i in range(size):
            for j in range(size):
                diagonals[i + j].append(matrix[i][j])

        return diagonals

    else:
        return matrix


def diagonals_print_v3(matrix):
    size = len(matrix)
    if size > 1:
        assert size == len(matrix[0]), "Please use square matrix"
        diagonals = []

        d = 0
        while True:
            diagonal = []
            i = 0
            j = d
            if j > size - 1:
                i = d - size + 1
                j = d - i

            while i < size and j >= 0:
                diagonal.append(matrix[i][j])
                i += 1
                j -= 1

            if len(diagonal) == 0:
                break

            diagonals.append(diagonal)
            d += 1

        return diagonals

    else:
        return matrix


def diagonals_print_v4(matrix):
    size = len(matrix)
    if size > 1:
        assert size == len(matrix[0]), "Please use square matrix"
        diagonals = []

        # param - auxiliary parameter for switching coordinates after secondary diagonal
        for param in range(2):
            for k in range(param, size):
                diagonal = []

                if param == 0:
                    i = 0
                    j = k
                    lim = 0
                else:
                    i = k
                    j = size - 1
                    lim = k

                while j >= lim:
                    diagonal.append(matrix[i][j])
                    i += 1
                    j -= 1
                diagonals.append(diagonal)

        return diagonals

    else:
        return matrix


if __name__ == '__main__':

    array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print(diagonals_print_v1(array))
    print(diagonals_print_v2(array))
    print(diagonals_print_v3(array))
    print(diagonals_print_v4(array))

    unittest.main()
