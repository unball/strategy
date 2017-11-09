from player import *
from math import pi
from math import fabs

class TestPlayer2(Player):
    def __init__(self):
        super(TestPlayer2, self).__init__()
        self.strategy = GoToBall2()

    def updateStrategy(self):
        pass

    def isInsideConeOfRadiusAndMaxDistance(self, angle_ball_to_player, radius = 30, maxDistance = 0.5):
        pass

    @property
    def TargetConeAngle(self):
        return (self.GoalCenter - self.ball).angle
