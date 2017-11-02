import math
from control_options import *
from ball import Ball
from robots_position import *

class Goalkeeper():
    global x
    global end_y
    x = 0.60
    y = 0
    end_y = 0.16
    control_option = control_options.position

    def __init__(self): #Set target
        self.x = x
        self.th = math.pi / 2
        #y_b = Ball.y
        #y_goalkeeper = Robot_Position.y[robot_id]

        # if (y_b > y_goalkeeper) and (y_b < end_y):
        #     self.y = y_b
        # if (y_b < y_goalkeeper) and (y_b > (-1) * end_y):
        #     self.y = y_b
        # if y_b > end_y:
        #     self.y = end_y
        # if y_b < (-1) * end_y:
        #     self.y = (-1) * end_y

    def getTarget(self):
        return self.x, self.y

    def getTh(self):
        return self.th

    def getControl_Option(self):
        return self.control_option
