import unittest
import math
from chess.board import Square

class TestSquare(unittest.TestCase):
    def test_example(self):
        self.assertTrue(True)

    def test_initial_distance(self):
        square = Square()
        self.assertEqual(square.distance, math.inf)

    def test_distance_only_set_once(self):
        square = Square()

        square.distance = 42
        square.distance = 9

        self.assertEqual(square.distance, 42)

    def test_string_output_infinite(self):
        square = Square()

        self.assertEqual(str(square), " ")

    def test_string_output_finite(self):
        square = Square()
        square.distance = 42

        self.assertEqual(str(square), "42")



