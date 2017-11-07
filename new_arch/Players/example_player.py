from player import *

class ExamplePlayer(Player):
    def __init__(self):
        self.strategy = AbstractStrategy()

    def updateStrategy(self):
        if (True == True):
            self.strategy = AbstractStrategy()