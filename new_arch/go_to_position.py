from abstract_strategy import *

class GoToPosition(AbstractStrategy):
    def __init__(self):
        self.ball_pos = Vec2()
        self.control_option = control_options.position
        self.position_options = [Point(0.5, 0.5), Point(0, 0.5), Point(-0.5, 0.5),
                                 Point(-0.5, -0.5), Point(0, -0.5), Point(0.5, -0.5)]
        self.keyboard_event = KEYBOARD_EVENT

    def get_strategy_output(self):
        return [self.goal.x, self.goal.y, 0, 0, 0, 0, 0, self.control_option]

    def calculate_goal(self):
        self.goal = position_options[self.keyboard_event]

        self.goal = Vec2(x, y)
