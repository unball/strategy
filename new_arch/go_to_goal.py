#!/usr/bin/env python
from control_options import *
import math
from abstract_strategy import *

def distance(vector1,vector2):
    distance = math.sqrt((vector1.x - vector2.x)**2 + (vector1.y - vector2.y)**2)
    return distance

class GoToGoal(AbstractStrategy):

    def __init__(self):

        self.ball_pos = Vec2()
        self.control_option = control_options.pose_line
        self.target_th = math.pi / 2
        self.end_y = 0.16
        self.goal_x = 0.60
        self.position = Vec2(0, 0)

    def get_strategy_output(self):
        return [self.goal.x, self.goal.y, self.target_th, 0, 0, 0, 0, self.control_option]

    def calculate_goal(self):
        if self.fieldSide == Side.RIGHT:
            self.orientation = 1
        else:
            self.orientation = -1

        self.referencePoint = Vec2(-0.75 * self.orientation, 0)
        distance_to_ball = distance(self.position, self.ball_pos)
        if distance_to_ball > 0.2:
            self.goal = Vec2(self.ball_pos.x, self.ball_pos.y)
        else:
            self.goal = self.referencePoint
