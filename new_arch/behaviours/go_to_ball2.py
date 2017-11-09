from abstract_strategy import *

class GoToBall2(AbstractStrategy):
    def __init__(self):
        self.ball_pos = Point(0, 0)
        self.control_option = control_options.position
        self.th = 0
        self.tolerance_radius = 0.2
        self.goal = Point(0, 0)
        self.lim_x = 0.35

    def get_strategy_output(self):
        return [self.goal.X, self.goal.Y, 0, self.u, 0, 0, 0, self.control_option]

    def calculate_goal(self):
        self.goal = Point(self.ball_pos.x, self.ball_pos.y)
        relative_target=convertTargetPositions(self.ball_pos.x, self.ball_pos.y, self.position.X, self.position.Y, self.th)
        if relative_target[1]>0:
            self.u=0
        if math.sqrt((self.ball_pos.x - self.position.X)**2 + (self.ball_pos.y - self.position.Y)**2) <= self.tolerance_radius:
            self.u=1
        if relative_target[1]<0:
            self.u=2

def convertTargetPositions(target_x, target_y, robot_x, robot_y, robot_th):
    relative_target = [target_x - robot_x, target_y - robot_y]
    relative_target = convert_axis_to_robot(relative_target, robot_th)
    return relative_target

def convert_axis_to_robot(vector, th):
    #Receive angle in radians
    ax = vector[0]
    ay = vector[1]

    y = ax*math.cos(th) + ay*math.sin(th)
    x = ax*math.sin(th) - ay*math.cos(th)

    return [x,y]