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

        self.assertEqual(actual, expected)

    def test_in_bounds_good(self):
        board = Board()

        actual = board.in_bounds(((1,2)))
        expected = ((1, 2))

        self.assertEqual(actual, expected)

    def test_in_bounds_bod(self):
        board = Board()

        actual = board.in_bounds(((-1,2)))
        expected = ()

        self.assertEqual(actual, expected)