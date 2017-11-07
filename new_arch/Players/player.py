from point import Point
from behaviours.circumvent_ball import CircumventBall
from behaviours.circumvent_ball import Direction
from behaviours.go_to_ball import *
from behaviours.go_to_position import *
from behaviours.go_to_goal import *
from behaviours.goalkeeper import *
from behaviours.control_test import *
from behaviours.look_to_target import *
from field_side import *

class Player(object):
    def __init__(self):
        self.pos = Point(0, 0)
        self.strategy = None
        self.target = [0, 0]
        self.th = 0
        self.control_option = 0
        self.ball = Point(0, 0)

    def getTarget(self):
        return self.target

    def getTh(self):
        return self.th

    def getControl_Option(self):
        return self.control_option

    def printValues(self):
        print self.target, self.th, self.control_option

    def set_own_state(self, x, y, th, robot_id):
        self.pos = Point(x, y)
        self.th = th
        self.robot_id = robot_id
        self.strategy.set_robot_state(self.pos, th, robot_id)

    def set_ball_state(self, ball):
        self.ball = ball
        self.strategy.set_ball_position(ball)

    def play(self):
        self.updateStrategy()
        self.strategy.calculate_goal()

    def goal(self):
        return self.strategy.get_strategy_output()

    def stop(self):
        return self.strategy.stop()

    def updateStrategy(self):
        pass

    @property
    def fieldSide(self):
        return FieldSide.side

    @property
    def GoalCenter(self):
        if self.fieldSide == Side.RIGHT:
            return Point(-0.75, 0)
        else:
            return Point(0.75, 0)