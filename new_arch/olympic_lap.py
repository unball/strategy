from control_options import *
from point import Point
from collections import deque

class OlympicLap():

    instructions = [Point(0.65, 0.55), Point(-0.65, 0.55),
                    Point(-0.65, -0.55), Point(0.65, -0.55)]

    dyn_instructions = deque(positions)

    def __init__(self):
        self.ball_pos = Point()
        self.control_option = control_options.position
        self.th = 0

    def set_robot_state(self, robot_point, robot_th, robot_id):
        self.position = robot_point
        self.robot_id = robot_id

    def set_ball_position(self, ball_pos):
        self.ball_pos = ball_pos

    def enemy_state(self, enemy_pos):
        pass

    def get_strategy_output(self):
        return [self.goal.x, self.goal.y, 0, 0, 0, 0, 0, self.control_option]

    def calculate_goal(self):
        if self.position == instructions[robot_id]
            instructions.rotate(1)

        self.goal = Point(instructions[self.robot_id].x, instructions[self.robot_id].y)
