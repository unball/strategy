from abstract_strategy import *
from math import pi
from enum import Enum
from math import fabs

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
        if fabs((self.target - self.position).angle - fabs(self.th*180/pi)) < 90:
            self.goal = (self.target - self.position).angle * pi/180
        else:
            self.goal = (self.target - self.position).angle * pi/180 + pi
