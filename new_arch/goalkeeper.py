import math
from point import Point
from control_options import *

class Goalkeeper():

    def __init__(self):
        self.ball_pos = Point()
        self.control_option = control_options.pose_line
        self.th = math.pi / 2
        self.end_y = 0.16
        self.goal_x = 0.60
        self.position = Point(0, 0)

    def set_robot_state(self, robot_point, robot_th, robot_id):
        self.position = robot_point

    def set_ball_position(self, ball_pos):
        self.ball_pos = ball_pos

    def enemy_state(self, enemy_pos):
        pass

    def get_strategy_output(self):
        return [self.goal.x, self.goal.y, self.th, 0, 0, 0, 0, self.control_option]

    def calculate_goal(self):
        if self.position.y <= self.ball_pos.y <= self.end_y:
            self.goal = Point(self.goal_x, self.ball_pos.y)

        if self.ball_pos.y > self.end_y:
            self.goal.y = self.end_y

        if (-1) * self.end_y <= self.ball_pos.y <= self.position.y:
            self.goal.y = self.ball_pos.y

        if self.ball_pos.y < (-1) * self.end_y:
            self.goal.y = (-1) * self.end_y
