# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        matrix = [[1, 2, 3, 4], [12, 13, 14, 5],
                  [11, 16, 15, 6], [10, 9, 8, 7]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        self.assertEqual(program.spiralTraverse(matrix), expected)
    
    def test_case_2(self):
        matrix = [[1]]
        expected = [1]
        print(program.spiralTraverse(matrix))
        self.assertEqual(program.spiralTraverse(matrix), expected)

    def test_case_8(self):
        matrix = [[1, 2, 3, 4], [10, 11, 12, 5], [9, 8, 7, 6]]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        print(program.spiralTraverse(matrix))
        self.assertEqual(program.spiralTraverse(matrix), expected)


if __name__ == "__main__":
    unittest.main()
