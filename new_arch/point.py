from planar import Vec2

class Point(Vec2):
    @property
    def X(self):
        return self.x

    @X.setter
    def X(self, value):
        self.__init__(value, self.y)

    @property
    def Y(self):
        return self.y

    @Y.setter
    def Y(self, value):
        self.__init__(self.x, value)

    @property
    def Quadrant(self):
        if self.angle < -90:
            return 3
        elif self.angle < 0:
            return 4
        elif self.angle < 90:
            return 1
        else:
            return 2