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

    def in_bounds(self, positions):
        return [p for p in positions if _is_in_bounds(p)]


def _is_in_bounds(position):
    return ((0 <= position[0] <= 7)
            and (0 <= position[1] <= 7))

def _chunks(squares):
    args = [iter(squares)] * 8
    return list(zip_longest(*args))


