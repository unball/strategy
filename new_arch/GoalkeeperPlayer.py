from player import *

class GoalkeeperPlayer(Player):
    def __init__(self):
        super(GoalkeeperPlayer, self).__init__()
        self.strategy = Goalkeeper()