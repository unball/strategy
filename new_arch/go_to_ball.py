from control_options import *
from ball import *

class Go_to_Ball():
    th = 0
    control_option = control_options.position

    def __init__(self, robot_id):
        self.x = Ball.x
        self.y = Ball.y

    def getTarget(self):
        return self.x, self.y

    def getTh(self):
        return self.th

    def getControl_Option(self):
        return self.control_option
