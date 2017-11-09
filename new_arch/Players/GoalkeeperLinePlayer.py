from player import *

class GoalkeeperLinePlayer(Player):
    def __init__(self):
        super(GoalkeeperLinePlayer, self).__init__()
        self.strategy = GoalkeeperLine()
