from abstract_strategy import *
from enum import Enum

class LookToTarget(AbstractStrategy):
    def __init__(self, target):
        self.ball_pos = Point(0, 0)
        self.control_option = control_options.angular_pose
        self.th = 0
        self.position = Point(0, 0)
        self.target = target

    def get_strategy_output(self):
        return [self.position.x, self.position.y, self.goal, 0, 0, 0, 0, self.control_option]

    def calculate_goal(self):
        self.goal = (self.position - self.target).angle

    @property
    def dTh(self):
        if self.direction == Direction.CLOCKWISE:
            return 180 - 180/6
        else:
            return -180 + 180/6
