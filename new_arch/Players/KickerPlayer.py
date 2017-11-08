from player import *
from math import pi
from math import fabs

class KickerPlayer(Player):
    def __init__(self):
        super(KickerPlayer, self).__init__()
        self.circumventStrategy = CircumventBall(radius=0.2)
        self.goToGoalStrategy = GoToPosition(self.GoalCenter)
        self.strategy = self.circumventStrategy
        self.lockCone = False
        self.lockCircle = False

    def updateStrategy(self):
        angle_ball_to_player = (self.ball - self.pos).angle
        if not self.isLocked:
            if self.isInsideConeOfRadiusAndMaxDistance(angle_ball_to_player, 30, 0.3):
                if self.isLooking():
                    self.strategy = self.goToGoalStrategy
                    self.lockCone = True
                else:
                    self.strategy = LookToTarget(self.ball)
            elif fabs(self.ball.distance_to(self.pos)) <= 0.5:
                self.circumventStrategy.changeDirection(self.getDirection())
                self.strategy = self.circumventStrategy
            else:
                self.strategy = GoToPosition(self.ball)
        if not self.isInsideConeOfRadiusAndMaxDistance(angle_ball_to_player, 45, 0.3):
            self.lockCone = False

    def isLooking(self):
        difference_angle = (self.ball - self.pos).angle*pi/180 - self.th
        return fabs(difference_angle) < 20*pi/180 or fabs(difference_angle) > pi - 20*pi/180

    def isInsideConeOfRadiusAndMaxDistance(self, angle_ball_to_player, angle = 30, maxDistance = 0.5):
        return fabs(angle_ball_to_player - self.TargetConeAngle) < angle and fabs(self.pos.distance_to(self.ball)) <= maxDistance

    @property
    def isLocked(self):
        return self.lockCone or self.lockCircle

    @property
    def TargetConeAngle(self):
        return (self.GoalCenter - self.ball).angle

    def getDirection(self):
        direction_vec2 = self.ball - self.GoalCenter
        direction_quadrant = Point(direction_vec2.x, direction_vec2.y).Quadrant
                
        difference = self.pos - self.ball
        angle_quadrant = Point(difference.x, difference.y).Quadrant

        if direction_quadrant == 2 and angle_quadrant == 3:
            return Direction.CLOCKWISE
        elif direction_quadrant == 2 and angle_quadrant == 1:
            return Direction.COUNTER_CLOCKWISE
        elif direction_quadrant == 3 and angle_quadrant == 4:
            return Direction.CLOCKWISE
        elif direction_quadrant == 3 and angle_quadrant == 2:
            return Direction.COUNTER_CLOCKWISE
        elif direction_quadrant == 4 and angle_quadrant == 1:
            return Direction.CLOCKWISE
        elif direction_quadrant == 4 and angle_quadrant == 3:
            return Direction.COUNTER_CLOCKWISE
        elif direction_quadrant == 1 and angle_quadrant == 2:
            return Direction.CLOCKWISE
        elif direction_quadrant == 1 and angle_quadrant == 4:
            return Direction.COUNTER_CLOCKWISE
        elif (difference.angle - direction_vec2.angle) <= 0:
            return Direction.COUNTER_CLOCKWISE

        return Direction.CLOCKWISE

    def reduce_angle(self,angle):
        while angle <= -180:
            angle += 2*180;
        while angle > 180:
            angle -= 2*180
        return angle;