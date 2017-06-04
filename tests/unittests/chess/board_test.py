import unittest
import math
from chess import Board

class TestBoard(unittest.TestCase):
    def test_example(self):
        self.assertTrue(True)

    def test_init(self):
        board = Board()

        actual = [x.distance for x in board.squares]
        expected = [math.inf for x in range(64)]
        expected[0] = 0

        self.assertEqual(actual, expected)

    def test_in_bounds_good(self):
        board = Board()

        actual = board.in_bounds([[1, 2]])
        expected = [[1, 2]]

        self.assertEqual(actual, expected)

    def test_in_bounds_bad_first(self):
        board = Board()

        actual = board.in_bounds([[-1, 2]])
        expected = []

        self.assertEqual(actual, expected)

    def test_in_bounds_bad_second(self):
        board = Board()

        actual = board.in_bounds([[1, -2]])
        expected = []

        self.assertEqual(actual, expected)

    def test_print(self):
        board = Board()
        self.maxDiff = None

        actual = str(board)
        expected = ("                                        \n"
                    "  *    *    *    *    *    *    *    *  \n"
                    "                                        \n"
                    "  *    *    *    *    *    *    *    *  \n"
                    "                                        \n"
                    "  *    *    *    *    *    *    *    *  \n"
                    "                                        \n"
                    "  *    *    *    *    *    *    *    *  \n"
                    "                                        \n"
                    "  *    *    *    *    *    *    *    *  \n"
                    "                                        \n"
                    "  *    *    *    *    *    *    *    *  \n"
                    "                                        \n"
                    "  *    *    *    *    *    *    *    *  \n"
                    "                                        \n"
                    "  0    *    *    *    *    *    *    *  \n")

        self.assertEqual(actual, expected)

