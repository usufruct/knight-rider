MOVES = (
    (1,2),
    (2,1),
    (2,-1),
    (1,-2),
    (-1,-2),
    (-2,-1),
    (-2,1),
    (-1,2),
)

class Knight:
    def __init__(self):
        pass

    def possible_moves(self, x, y):
        return [[m[0] + x, m[1] + y] for m in MOVES]
