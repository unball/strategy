from abstract_strategy import *

class GoToBall(AbstractStrategy):
    def __init__(self):
        self.ball_pos = Point()
        self.control_option = control_options.pose
        self.th = 0

    def get_strategy_output(self):
        return [self.goal.x, self.goal.y, 0, 0, 0, 0, 0, self.control_option]

    def calculate_goal(self):
        self.goal = Point(self.ball_pos.x, self.ball_pos.y)
