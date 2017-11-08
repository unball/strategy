from abstract_strategy import *

class GoToPosition(AbstractStrategy):
    def __init__(self, point):
        self.ball_pos = Point(0, 0)
        self.control_option = control_options.pose_line
        self.x = point.x
        self.y = point.y

    def get_strategy_output(self):
        return [self.goal.x, self.goal.y, 0, 0, 0, 0, 0, self.control_option]

    def calculate_goal(self):
        self.goal = Point(self.x, self.y)
