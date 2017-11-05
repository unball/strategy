from abstract_strategy import *
from collections import deque

class OlympicLap():

    instructions = [Point(0.65, 0.55), Point(-0.65, 0.55),
                    Point(-0.65, -0.55), Point(0.65, -0.55)]

    dyn_instructions = deque(positions)

    def __init__(self):
        self.ball_pos = Point()
        self.control_option = control_options.position

    def get_strategy_output(self):
        return [self.goal.x, self.goal.y, 0, 0, 0, 0, 0, self.control_option]

    def calculate_goal(self):
        if self.position == instructions[robot_id]
            instructions.rotate(1)

        self.goal = Point(instructions[self.robot_id].x, instructions[self.robot_id].y)
