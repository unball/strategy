from abstract_strategy import *
from math import pi

class CircumventBall(AbstractStrategy):
    def __init__(self):
        self.ball_pos = Point(0, 0)
        self.control_option = control_options.position
        self.th = 0
        self.position = Point(0, 0)

    def get_strategy_output(self):
        return [self.goal.x, self.goal.y, 0, 0, 0, 0, 0, self.control_option]

    def calculate_goal(self):
        diff_angle = (self.ball_pos - self.position).angle
        radius = (self.ball_pos - self.position).length
        target = Point.polar(diff_angle + pi/4, radius)
        self.goal = target + self.ball_pos
