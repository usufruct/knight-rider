import unittest
from chess import Knight

class TestKnight(unittest.TestCase):
    def test_example(self):
        self.assertTrue(True)

    def test_possible_moves_from_zero(self):
        knight = Knight([0,0])

        actual = knight.possible_moves()
        expected = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]

        self.assertEqual(actual, expected)

    def test_possible_moves_from_location(self):
        knight = Knight([1,0])

        actual = knight.possible_moves()
        expected = [[2, 2], [3, 1], [3, -1], [2, -2], [0, -2], [-1, -1], [-1, 1], [0, 2]]

        self.assertEqual(actual, expected)


