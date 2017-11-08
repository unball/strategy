from abstract_strategy import *

class ExampleStrategy(AbstractStrategy):
    def __init__(self):
        self.ball_pos = Point(0, 0)
        self.control_option = control_options.position

    def get_strategy_output(self):
        return [self.goal.x, self.goal.y, 0, 0, 0, 0, 0, self.control_option]

    def calculate_goal(self):
        self.goal = Point(0, 0)
