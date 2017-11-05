from abstract_strategy import *

class Goalkeeper(AbstractStrategy):

    def __init__(self):
        self.ball_pos = Point()
        self.control_option = control_options.pose_line
        self.target_th = math.pi / 2
        self.end_y = 0.16
        self.goal_x = 0.60
        self.position = Point(0, 0)

    def get_strategy_output(self):
        return [self.goal.x, self.goal.y, self.target_th, 0, 0, 0, 0, self.control_option]

    def calculate_goal(self):
        if self.fieldSide == Side.RIGHT:
            self.goal_x = 0.60

        if self.fieldSide == Side.LEFT:
            self.goal_x = -0.60

        if self.position.y <= self.ball_pos.y <= self.end_y:
            self.goal = Point(self.goal_x, self.ball_pos.y)

        if self.ball_pos.y > self.end_y:
            self.goal.y = self.end_y

        if (-1) * self.end_y <= self.ball_pos.y <= self.position.y:
            self.goal.y = self.ball_pos.y

        if self.ball_pos.y < (-1) * self.end_y:
            self.goal.y = (-1) * self.end_y
