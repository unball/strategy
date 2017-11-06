from player import *
from math import pi
from math import fabs

class KickerPlayer(Player):
    def __init__(self):
        super(KickerPlayer, self).__init__()
        self.strategy = CircumventBall(Direction.COUNTER_CLOCKWISE)

    def updateStrategy(self):
        angle_ball_to_player = (self.ball - self.pos).angle
        if fabs(angle_ball_to_player - self.TargetConeAngle) < 45 and self.strategy.name != 'GoToPosition':
            print('position')
            #self.strategy = GoToPosition()
        elif self.strategy.name != 'Circumvent':
            print('circ')
            #self.strategy = CircumventBall(Direction.COUNTER_CLOCKWISE)

    @property
    def GoalCenter(self):
        if self.fieldSide == Side.RIGHT:
            return Point(0.75, 0)
        else:
            return Point(-0.75, 0)

    @property
    def TargetConeAngle(self):
        return (self.GoalCenter - self.ball).angle