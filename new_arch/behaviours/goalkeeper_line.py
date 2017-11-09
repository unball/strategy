from abstract_strategy import *

class GoalkeeperLine(AbstractStrategy):

    def __init__(self):
        self.ball_pos = Point(0, 0)
        self.control_option = control_options.pose_line
        self.target_th = math.pi / 2
        self.end_y = 0.16
        self.position = Point(0, 0)
        self.goal = Point(0, 0)
        self.tolerance_radius = 0.1

    def get_strategy_output(self):
        return [self.goal.X, self.goal.Y, self.target_th, 0, 0, 0, 0, self.control_option]

    def calculate_goal(self):
        if math.sqrt((self.ball_pos.X - self.position.X)**2 + (self.ball_pos.Y - self.position.Y)**2) <= self.tolerance_radius:
            if self.fieldSide == Side.RIGHT:
                self.u = 3
            if self.fieldSide == Side.LEFT:
                self.u = 4

        else:
            if self.fieldSide == Side.RIGHT:
                self.goal.X = 0.60
            if self.fieldSide == Side.LEFT:
                self.goal.X = -0.60

            if self.position.Y <= self.ball_pos.Y <= self.end_y:
                self.goal.Y = self.ball_pos.Y

            if self.ball_pos.Y > self.end_y:
                self.goal.Y = self.end_y

            if (-1) * self.end_y <= self.ball_pos.Y <= self.position.Y:
                self.goal.Y = self.ball_pos.Y

            if self.ball_pos.Y < (-1) * self.end_y:
                self.goal.Y = (-1) * self.end_y
