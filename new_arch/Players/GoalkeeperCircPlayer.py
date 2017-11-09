from player import *

class GoalkeeperCircPlayer(Player):
    def __init__(self):
        super(GoalkeeperCircPlayer, self).__init__()
        self.strategy = Goalkeeper()
