from point import Point
from Players.KickerPlayer import KickerPlayer
from Players.GoalkeeperPlayer import GoalkeeperPlayer
from Players.TestPlayer import TestPlayer
from Players.SquareKicker import SquareKicker
from Players.SimpleKicker import SimpleKicker

class Team():
    def __init__(self):
        self.players = [TestPlayer(), SimpleKicker(), GoalkeeperPlayer()]
        self.ball = Point(0, 0)
        self.robots_pos_x = []
        self.robots_pos_y = []
        self.robots_th = []
        self.v = []
        self.w = []
        self.vx = []
        self.vy = []
        self.strategy_output = []
        self.ball_walls = Point(0, 0)

    def set_params(self, ball, robots_pos_x, robots_pos_y, robots_th, ball_x_walls, ball_y_walls):
        self.robots_pos_x = robots_pos_x
        self.robots_pos_y = robots_pos_y
        self.robots_th = robots_th
        self.ball = ball
        self.ball_walls.X = ball_x_walls
        self.ball_walls.Y = ball_y_walls

    def run(self):
        for player, pos_x, pos_y, th in zip(self.players, self.robots_pos_x,
                                            self.robots_pos_y, self.robots_th):
            robot_id = self.players.index(player)
            player.set_own_state(pos_x, pos_y, th, robot_id)
            player.set_ball_state(self.ball, self.ball_walls)

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
