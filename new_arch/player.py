from point import Point

class Player(object):
    target = [0, 0]
    th = 0
    control_option = 0

    def __init__(self, strategy):
        self.pos = Point()
        self.strategy = strategy
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
        self.strategy.calculate_goal()

    def goal(self):
        return self.strategy.get_strategy_output()

    def stop(self):
        return self.strategy.stop()