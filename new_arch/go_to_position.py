from abstract_strategy import *

class GoToPosition(AbstractStrategy):
    def __init__(self):
        self.ball_pos = Vec2()
        self.control_option = control_options.position

    def get_strategy_output(self):
        return [self.goal.x, self.goal.y, 0, 0, 0, 0, 0, self.control_option]

    def calculate_goal(self):
        x = 0
        y = 0
        self.goal = Vec2(x, y)
