import unittest
from chess import traverse_board, knights_on_point, Board

class TraverseBoardTest(unittest.TestCase):
    def test_example(self):
        self.assertTrue(True)

    def test_knights_on_point(self):
        board = Board()
        board.squares[3].distance = 4
        board.squares[42].distance = 4

        actual = [k.position for k in knights_on_point(board)]
        expected = [[3, 0], [2, 5]]

        self.assertEqual(actual, expected)

    def test_traverse_board(self):
        board = Board()
        knights = knights_on_point(board)

        traverse_board(board, knights)

        self.assertEqual(board.square_at_position([1,2]).distance, 1)
        self.assertEqual(board.square_at_position([2,1]).distance, 1)


