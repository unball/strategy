from control_options import *
from ball import *

class Go_to_Position():
    th = 0
    control_option = control_options.pose

    def __init__(self, robot_id, x, y):
        self.x = x
        self.y = y

    def getTarget(self):
        return self.x, self.y

    def getTh(self):
        return self.th

    def getControl_Option(self):
        return self.control_option
