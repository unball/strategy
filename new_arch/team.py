from point import Point
from Players.KickerPlayer import KickerPlayer
from Players.GoalkeeperPlayer import GoalkeeperPlayer
from Players.TestPlayer import TestPlayer

class Team():
    def __init__(self):
        self.players = [KickerPlayer(), GoalkeeperPlayer(), GoalkeeperPlayer()]
        self.ball = Point(0, 0)
        self.robots_pos_x = []
        self.robots_pos_y = []
        self.robots_th = []
        self.v = []
        self.w = []
        self.vx = []
        self.vy = []
        self.strategy_output = []

    def set_params(self, ball, robots_pos_x, robots_pos_y, robots_th):
        self.robots_pos_x = robots_pos_x
        self.robots_pos_y = robots_pos_y
        self.robots_th = robots_th
        self.ball = ball

    def run(self):
        for player, pos_x, pos_y, th in zip(self.players, self.robots_pos_x,
                                            self.robots_pos_y, self.robots_th):
            robot_id = self.players.index(player)
            player.set_own_state(pos_x, pos_y, th, robot_id)
            player.set_ball_state(self.ball)

        for player in self.players:
            player.play()
            self.strategy_output.append(player.goal())

    def stop(self):
        for player, pos_x, pos_y, th in zip(self.players, self.robots_pos_x,
                                            self.robots_pos_y, self.robots_th):
            robot_id = self.players.index(player)
            player.set_own_state(pos_x, pos_y, th, robot_id)
            self.strategy_output.append(player.stop())

    def output(self):
        output = self.strategy_output
        self.strategy_output = []
        return output
