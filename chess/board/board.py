from .square import Square

class Board:
    def __init__(self):
        self.squares = [Square() for x in range(64)]

    def in_bounds(self, positions):
        return positions