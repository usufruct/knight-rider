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
        return tuple([tuple([p[0] + x, p[1] + y]) for p in MOVES])
