import math
from itertools import zip_longest
from .square import Square

class Board:
    def __init__(self):
        self.squares = [Square() for x in range(64)]
        self.squares[0].distance = 0

    def __str__(self):
        squares = [str(s) for s in self.squares]
        chunks = reversed(_chunks(squares))
        result = ""
        for chunk in chunks:
            result = result  + ("     " * 8) + "\n"
            result = result + "".join([ "  " + x + "  " for x in chunk]) + "\n"
        return result

    def square_at_position(self, position):
        x = position[0]
        y = position[1]
        index = (8 * y) + x

        return self.squares[index]

    def index_to_position(self, index):
        return [index % 8, index // 8]

    def biggest_measured_distance(self):
        distances = [s.distance for s in self.squares]
        measured_distances = [d for d in distances if d != math.inf]

        return sorted(measured_distances, reverse=True)[0]

    def in_bounds(self, positions):
        return [p for p in positions if _is_in_bounds(p)]

    def infinite_positions(self, positions):
        return [p for p in positions if self.square_at_position(p).distance == math.inf]

    def positions_matching_distance(self, distance):
        results = []
        for index, square in enumerate(self.squares):
            if square.distance == distance:
                results.append(self.index_to_position(index))

        return results


    def incomplete(self):
        distances = [s.distance for s in self.squares]

        return sorted(distances, reverse=True)[0] == math.inf

def _is_in_bounds(position):
    return ((0 <= position[0] <= 7)
            and (0 <= position[1] <= 7))

def _chunks(squares):
    args = [iter(squares)] * 8
    return list(zip_longest(*args))


