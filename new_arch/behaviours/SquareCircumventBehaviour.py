from abstract_strategy import *
from enum import Enum
from field_side import *
from planar import Vec2
from math import fabs

class Direction(Enum):
    CLOCKWISE = 1
    COUNTER_CLOCKWISE = -1

class SquareCircumventBehaviour(AbstractStrategy):
    def __init__(self, direction = Direction.CLOCKWISE, radius = 0.5):
        self.ball_pos = Point(0, 0)
        self.control_option = control_options.position
        self.th = 0
        self.position = Point(0, 0)
        self.direction = direction
        self.radius = radius
        self.goal = Point(0, 0)
        self.temp_goal = None
        self.dTh = 0

    def get_strategy_output(self):
        if self.temp_goal == None:
            return [self.goal.x, self.goal.y, 0, 0, 0, 0, 0, self.control_option]
        else:
            return [self.temp_goal.x, self.temp_goal.y, 0, 0, 0, 0, 0, self.control_option]

    def calculate_goal(self):
        target = self.ball_pos - Point.polar(self.TargetConeAngle, self.radius)
        
        if self.isInCone(target) and self.position.distance_to(self.goal) < 0.1:
            self.temp_goal = self.get_counter_side()
        elif self.temp_goal != None and self.position.distance_to(self.temp_goal) < 0.15:
            self.temp_goal = None
        self.goal = target

    def isInCone(self, target):
        return self.isInsideConeOfRadiusAndMaxDistance(target=self.position,start=self.ball_pos,angle=30,maxDistance=target.distance_to(self.position))

    def get_counter_side(self):
        error = fabs((self.position - self.ball_pos).angle + self.TargetConeAngle)
        #error = (self.position - self.ball_pos).angle
        
        trigger = 0
        if self.dTh == 90:
            trigger = 30
        elif self.dTh == -90:
            trigger = -30
        
        if error > trigger:
            self.dTh = -90
        elif error <= trigger:
            self.dTh = 90
        angle = -self.TargetConeAngle + self.dTh
        return Point.polar(angle, 0.2) + self.ball_pos

    @property
    def TargetConeAngle(self):
        return (self.GoalCenter - self.ball_pos).angle

    def isInsideConeOfRadiusAndMaxDistance(self, target, start, angle = 45, maxDistance = 0.5):
        angle_target_to_player = (target - start).angle
        isInsideCone = (fabs(angle_target_to_player) < angle or fabs(angle_target_to_player) > 180 - angle)
        return isInsideCone and fabs(start.distance_to(target)) <= maxDistance

    @property
    def GoalCenter(self):
        if FieldSide.side == Side.RIGHT:
            return Point(-0.85, 0)
        else:
            return Point(0.85, 0)