from player import *
from math import pi
from math import fabs

class SimpleKicker(Player):
    def __init__(self):
        super(SimpleKicker, self).__init__()
        self.strategy = GoToPosition(self.behindTheBall())
        self.reachedGoal = False
        self.pos = Point(100,100)
        self.ball = Point(-100,-100)

    def updateStrategy(self):
        if (self.ball.x == -100 and self.ball.y == -100):
            self.strategy = GoToPosition(self.behindTheBall())
            self.reachedGoal = False

        angle_ball_to_player = (self.ball - self.pos).angle

        if self.reachedGoal == True:
            self.strategy = GoToPosition(self.GoalCenter)

        if self.pos.distance_to(self.behindTheBall()) < 0.1 and self.reachedGoal == False:
            self.reachedGoal = True
        if self.isInsideConeOfRadiusAndMaxDistance(angle_ball_to_player, angle = 45) == False and self.pos.distance_to(self.behindTheBall()) > 0.3:
            self.reachedGoal = False
            self.strategy = GoToPosition(self.behindTheBall())


    def behindTheBall(self):
        return self.ball - Point.polar(self.TargetConeAngle, 0.25)

    def isInsideConeOfRadiusAndMaxDistance(self, angle_ball_to_player, angle = 30, maxDistance = 0.5):
        return fabs(angle_ball_to_player - self.TargetConeAngle) < angle and fabs(self.pos.distance_to(self.ball)) <= maxDistance

    def goal(self):
        if self.fieldSide == Side.RIGHT:
            if (self.strategy.goal.x > 0.5):
                self.strategy.goal.X = 0.5
                self.reachedGoal = False
        else:
            if (self.strategy.goal.x < -0.5):
                self.strategy.goal.X = -0.5
                self.reachedGoal = False

        return self.strategy.get_strategy_output()

    @property
    def TargetConeAngle(self):
        return (self.GoalCenter - self.ball).angle