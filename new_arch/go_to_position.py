from control_options import *
from point import Point

class GoToPosition():
    def __init__(self):
        self.ball_pos = Point()
        self.control_option = control_options.position
        self.th = 0

    def set_robot_state(self, robot_point, robot_th):
        pass

    def set_ball_position(self, ball_pos):
        self.ball_pos = ball_pos

    def enemy_state(self, enemy_pos):
        pass

    def get_strategy_output(self):
        return [self.goal.x, self.goal.y, 0, 0, 0, 0, 0, self.control_option]

    def calculate_goal(self):
        x = 0
        y = 0

        self.goal = Point(x, y)
