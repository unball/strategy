from abstract_strategy import *
from enum import Enum

class Direction(Enum):
    CLOCKWISE = 1
    COUNTER_CLOCKWISE = -1

class CircumventBall(AbstractStrategy):
    def __init__(self, direction = Direction.CLOCKWISE, radius = 0.5):
        self.ball_pos = Point(0, 0)
        self.control_option = control_options.position
        self.th = 0
        self.position = Point(0, 0)
        self.direction = direction
        self.radius = radius

    def get_strategy_output(self):
        return [self.goal.x, self.goal.y, 0, 0, 0, 0, 0, self.control_option]

    def calculate_goal(self):
        diff_angle = (self.ball_pos - self.position).angle
        target = Point.polar(diff_angle + self.dTh, self.radius)
        self.goal = target + self.ball_pos

    def changeDirection(self, newDirection):
        self.direction = newDirection

    @property
    def dTh(self):
        if self.direction == Direction.CLOCKWISE:
            return 180 - 180/4
        else:
            return -180 + 180/4
