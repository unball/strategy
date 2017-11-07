from player import *
from math import pi
from math import fabs

class KickerPlayer(Player):
    def __init__(self):
        super(KickerPlayer, self).__init__()
        self.circumventStrategy = CircumventBall(Direction.COUNTER_CLOCKWISE)
        self.goToPositionStrategy = GoToPosition()
        self.strategy = self.circumventStrategy

    def updateStrategy(self):
        angle_ball_to_player = (self.ball - self.pos).angle
        if self.isInsideConeOfRadiusAndMaxDistance(angle_ball_to_player, 30, 0.3):
            self.strategy = self.goToPositionStrategy
        elif self.strategy.name:
            self.strategy = self.circumventStrategy

    def isInsideConeOfRadiusAndMaxDistance(self, angle_ball_to_player, radius = 30, maxDistance = 0.5):
        return fabs(angle_ball_to_player - self.TargetConeAngle) < radius and fabs(self.pos.distance_to(self.ball)) <= maxDistance

    @property
    def GoalCenter(self):
        if self.fieldSide == Side.RIGHT:
            return Point(0.75, 0)
        else:
            return Point(-0.75, 0)

    @property
    def TargetConeAngle(self):
        return (self.GoalCenter - self.ball).angle
