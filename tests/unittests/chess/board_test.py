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

    def test_infinite_positions_yes(self):
        board = Board()

        actual = board.infinite_positions([[1, 2]])
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

    def test_square_at_position_zero(self):
        board = Board()

        actual = board.square_at_position([0,0])
        expected = board.squares[0]

        self.assertEqual(actual, expected)

    def test_square_at_position_42(self):
        board = Board()

        actual = board.square_at_position([2,5])
        expected = board.squares[42]

        self.assertEqual(actual, expected)

    def test_index_to_position_zero(self):
        board = Board()

        actual = board.index_to_position(0)
        expected = [0, 0]

        self.assertEqual(actual, expected)

    def test_index_to_position_42(self):
        board = Board()

        actual = board.index_to_position(42)
        expected = [2, 5]

        self.assertEqual(actual, expected)

    def test_incomplete_true(self):
        board = Board()

        self.assertTrue(board.incomplete())

    def test_incomplete_false(self):
        board = Board()
        for i in range(64):
            board.squares[i].distance = 666

        self.assertFalse(board.incomplete())

    def test_biggest_measured_distance_zero(self):
        board = Board()

        actual = board.biggest_measured_distance()
        expected = board.squares[0].distance

        self.assertEqual(actual, expected)

    def test_biggest_measured_distance_amount(self):
        board = Board()
        board.squares[6].distance = 100

        actual = board.biggest_measured_distance()
        expected = 100

        self.assertEqual(actual, expected)

    def test_positions_matching_distance(self):
        board = Board()
        board.squares[7].distance = 42
        board.squares[15].distance = 42

        actual = board.positions_matching_distance(42)
        expected = [[7, 0], [7, 1]]

        self.assertEqual(actual, expected)

    def test_print(self):
        board = Board()
        self.maxDiff = None

        actual = str(board)
        expected = ("                                        \n"
                    "                                        \n"
                    "                                        \n"
                    "                                        \n"
                    "                                        \n"
                    "                                        \n"
                    "                                        \n"
                    "                                        \n"
                    "                                        \n"
                    "                                        \n"
                    "                                        \n"
                    "                                        \n"
                    "                                        \n"
                    "                                        \n"
                    "                                        \n"
                    "  0                                     \n")

        self.assertEqual(actual, expected)

