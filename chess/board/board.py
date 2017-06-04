from .square import Square

class Board:
    def __init__(self):
        self.squares = [Square() for x in range(64)]
        # (0 <= postion[0] <= 7) && (0 <= postion[1] <= 7)

    def in_bounds(self, positions):
        return [p for p in positions if _is_in_bounds(p)]


def _is_in_bounds(position):
    return ((0 <= position[0] <= 7)
            and (0 <= position[1] <= 7))
