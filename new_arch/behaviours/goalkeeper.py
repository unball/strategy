from abstract_strategy import *

def dislocate(original_point, dist_dislocated):
    return Point(original_point.X + dist_dislocated, original_point.Y)

class Goalkeeper(AbstractStrategy):

    def __init__(self):
        self.ball_pos = Point(0, 0)
        self.control_option = control_options.pose_line
        self.target_th = math.pi / 2
        self.end_y = 0.16
        self.position = Point(0, 0)
        self.goal = Point(0, 0)
        self.circ_radius = 0.5
        self.circ_center_x = 1.1
        self.tolerance_radius = 0.1
        self.saturatorR = 2.5
        self.saturatorL = math.pi - self.saturatorR

    def get_strategy_output(self):
        if self.is_ball_wall_in_goal_range():
            return [self.goal.X, self.ball_wall.y, self.target_th, self.u, 0, 0, 0, self.control_option]
        return [self.goal.X, self.goal.Y, self.target_th, self.u, 0, 0, 0, self.control_option]

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
            if self.fieldSide == Side.RIGHT:
                dislocated_ball = dislocate(self.ball_pos, -self.circ_center_x)
                th = math.atan2(dislocated_ball.Y, dislocated_ball.X)

                if math.fabs(th) < self.saturatorR:
                    if self.goal.Y > 0:
                        th = self.saturatorR
                    if self.goal.Y < 0:
                        th = (-1) * self.saturatorR

                aux_target = Point(self.circ_radius * math.cos(th), self.circ_radius * math.sin(th))
                self.goal = dislocate(aux_target, self.circ_center_x)
                self.u = 0

            if self.fieldSide == Side.LEFT:

                dislocated_ball = dislocate(self.ball_pos, self.circ_center_x)
                th = math.atan2(dislocated_ball.Y, dislocated_ball.X)

                if math.fabs(th) > self.saturatorL:
                    if self.goal.Y > 0:
                        th = self.saturatorL
                    if self.goal.Y < 0:
                        th = (-1) * self.saturatorL

                aux_target = Point(self.circ_radius * math.cos(th), self.circ_radius * math.sin(th))
                self.goal = dislocate(aux_target, -self.circ_center_x)
                self.u = 0

    def is_ball_wall_in_goal_range(self):
        print(self.ball_wall)
        if FieldSide.side == Side.RIGHT:
            if self.ball_wall.x >= 0.6 and (self.ball_wall.y < 0.7 and self.ball_wall.y > -0.7):
                print('true')
                return True
        else:
            if self.ball_wall.x <= -0.6 and (self.ball_wall.y < 0.7 and self.ball_wall.y > -0.7):
                print('true')
                return True
        return False