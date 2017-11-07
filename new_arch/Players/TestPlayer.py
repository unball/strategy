from player import *
from math import pi
from math import fabs

class TestPlayer(Player):
    def __init__(self):
        super(TestPlayer, self).__init__()
        self.strategy = ControlTest()

    def updateStrategy(self):
        pass

    def isInsideConeOfRadiusAndMaxDistance(self, angle_ball_to_player, radius = 30, maxDistance = 0.5):
        pass

    @property
    def TargetConeAngle(self):
        return (self.GoalCenter - self.ball).angle
