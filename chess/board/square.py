import math

class Square:
    def __init__(self):
        self._distance = math.inf

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        if self._distance == math.inf:
            self._distance = value