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
