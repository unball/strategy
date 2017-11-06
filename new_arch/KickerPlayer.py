from player import *

class KickerPlayer(Player):
    def __init__(self):
        super(KickerPlayer, self).__init__()
        self.strategy = CircumventBall(Direction.COUNTER_CLOCKWISE)

    def updateStrategy(self):
        pass