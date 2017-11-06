from player import Player

class KickerPlayer(object):
    def __init__(self, strategy):
        super(KickerPlayer, self).__init__()
        self.strategy = strategy