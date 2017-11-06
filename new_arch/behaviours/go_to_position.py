from abstract_strategy import *

class GoToPosition(AbstractStrategy):
    def __init__(self):
        self.ball_pos = Point(0, 0)
        self.control_option = control_options.position
        self.name = 'GoToPosition'
        print("GO TO POSITION MOTHERFUCKER")

    def get_strategy_output(self):
        return [self.goal.x, self.goal.y, 0, 0, 0, 0, 0, self.control_option]

    def calculate_goal(self):
        x = 0.75
        y = 0
        self.goal = Point(x, y)
