import math
from point import Point
from control_options import *
from field_side import *

class AbstractStrategy():

    def set_robot_state(self, robot_point, robot_th, robot_id):
        self.position = robot_point
        self.th = robot_th
        self.id = robot_id
        self.name = 'Abstract'

    def set_ball_position(self, ball_pos):
        self.ball_pos = ball_pos

    def enemy_state(self, enemy_pos):
        pass

    def stop(self):
        return [self.position.x, self.position.y, self.th, 0, 0, 0, 0, control_options.direct_speeds]

    @property
    def fieldSide(self):
        return FieldSide.side
