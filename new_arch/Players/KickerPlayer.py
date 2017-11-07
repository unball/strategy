from player import *
from math import pi
from math import fabs

class KickerPlayer(Player):
    def __init__(self):
        super(KickerPlayer, self).__init__()
        self.circumventStrategy = CircumventBall(radius=0.2)
        self.goToGoalStrategy = GoToPosition(self.GoalCenter)
        self.strategy = self.circumventStrategy
        self.counter = 0

    def updateStrategy(self):
        angle_ball_to_player = (self.ball - self.pos).angle
        self.counter = self.counter + 1
        if self.isInsideConeOfRadiusAndMaxDistance(angle_ball_to_player, 45, 0.5):
            print(angle_ball_to_player)
            #if 180 - angle_ball_to_player > 20:
            #    print('look')
            #    self.strategy = LookToTarget(self.ball)
            #else:
            print('goal', self.counter)
            self.strategy = self.goToGoalStrategy
        elif fabs(self.ball.distance_to(self.pos)) <= 0.3:
            print('circ', self.counter)
            self.strategy = self.circumventStrategy
        else:
            print('ball', self.counter)
            self.strategy = GoToPosition(self.ball)

    def isInsideConeOfRadiusAndMaxDistance(self, angle_ball_to_player, radius = 30, maxDistance = 0.5):
        return fabs(angle_ball_to_player - self.TargetConeAngle) < radius and fabs(self.pos.distance_to(self.ball)) <= maxDistance

    @property
    def TargetConeAngle(self):
        return (self.GoalCenter - self.ball).angle
