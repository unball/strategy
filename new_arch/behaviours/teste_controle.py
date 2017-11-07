from abstract_strategy import *

class TesteControle(AbstractStrategy):
    def __init__(self):
        self.ball_pos = Point(0, 0)
        self.control_option = control_options.position
        self.name = 'GoToPosition'
        self.position_options = [Point(0.5, 0.5), Point(0, 0.5), Point(-0.5, 0.5),
                                 Point(-0.5, -0.5), Point(0, -0.5), Point(0.5, -0.5)]

    def get_strategy_output(self):
        return [self.goal.x, self.goal.y, 0, 0, 0, 0, 0, self.control_option]
s
    def calculate_goal(self):
        self.goal = self.position_options[Keyboard.EVENT]
