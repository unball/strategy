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
    def GoalCenter(self):
        if self.fieldSide == Side.RIGHT:
            return Point(0.75, 0)
        else:
            return Point(-0.75, 0)

    @property
    def TargetConeAngle(self):
        return (self.GoalCenter - self.ball).angle
