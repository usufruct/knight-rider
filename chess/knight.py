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
    def __init__(self, position):
        self.position = position

    def possible_moves(self):
        x = self.position[0]
        y = self.position[1]
        return [[m[0] + x, m[1] + y] for m in MOVES]
