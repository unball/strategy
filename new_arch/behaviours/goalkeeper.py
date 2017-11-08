from abstract_strategy import *

class Goalkeeper(AbstractStrategy):

    def __init__(self):
        self.ball_pos = Point(0, 0)
        self.control_option = control_options.pose_line
        self.target_th = math.pi / 2
        self.end_y = 0.16
        self.position = Point(0, 0)
        self.goal = Point(0, 0)
        self.radius = 0.15

    def get_strategy_output(self):
        return [self.goal.X, self.goal.Y, self.target_th, 0, 0, 0, 0, self.control_option]

    def calculate_goal(self):
        if self.fieldSide == Side.RIGHT:
            fakeball_x = math.fabs(self.ball_pos.X)
            desloc_x = -0.7
            fakeball_x = fakeball_x + desloc_x

            th = math.atan2(self.ball_pos.Y, fakeball_x)
            self.goal = Point(self.radius * math.cos(th) - desloc_x, self.radius * math.sin(th))

            print fakeball_x #TODO fix for x < 0 (ircle center in the opposite goal)
            print self.ball_pos.X
            print "-------------------"

        if self.fieldSide == Side.LEFT: #TODO implement the same logic to the LEFT side as the RIGHT side of the field
        pass
