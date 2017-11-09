from abstract_strategy import *

class GoToBall(AbstractStrategy):
    def __init__(self):
        self.ball_pos = Point(0, 0)
        self.control_option = control_options.pose_line
        self.th = 0
        self.tolerance_radius = 0.1
        self.goal = Point(0, 0)

    def get_strategy_output(self):
        return [self.goal.X, self.goal.Y, 0, self.u, 0, 0, 0, self.control_option]

    def calculate_goal(self):
        if math.sqrt((self.ball_pos.X - self.position.X)**2 + (self.ball_pos.Y - self.position.Y)**2) <= self.tolerance_radius:
            if self.fieldSide == Side.RIGHT:
                if self.ball_pos.Y > 0:
                    self.u = 4
                else:
                    self.u = 3

            if self.fieldSide == Side.LEFT:
                if self.ball_pos.Y > 0:
                    self.u = 3
                else:
                    self.u = 4
        else:
            self.goal = Point(self.ball_pos.x, self.ball_pos.y)
            self.u = 0
