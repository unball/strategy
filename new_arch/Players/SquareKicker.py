from player import *
from math import pi
from math import fabs

class SquareKicker(Player):
    def __init__(self):
        super(SquareKicker, self).__init__()
        self.circumventStrategy = SquareCircumventBehaviour(radius=0.15)
        self.goToGoalStrategy = GoToPosition(self.GoalCenter)
        self.strategy = self.circumventStrategy

    def updateStrategy(self):
        if self.circumventStrategy.goal.distance_to(self.pos) < 0.1:
            self.strategy = self.goToGoalStrategy
        elif fabs(self.ball.distance_to(self.pos)) <= 0.5:
            self.strategy = self.circumventStrategy
        else:
            self.strategy = GoToPosition(self.ball)