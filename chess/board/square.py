import math

class Square:
    def __init__(self):
        self._distance = math.inf

    def __str__(self):
        if self.distance == math.inf:
            return "*"
        else:
            return str(self.distance)

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        if self._distance == math.inf:
            self._distance = value