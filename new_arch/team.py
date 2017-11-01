from player import *
from goalkeeper import *

robot_id = [0, 1, 2]
number_of_robots = 3

class Team():

    x = [0, 0, 0]
    y = [0, 0, 0]
    th = [0, 0, 0]
    w = [0 ,0 ,0]
    v = [0 ,0 ,0]
    vx = [0 ,0 ,0]
    vy = [0 ,0 ,0]
    control_option = [0, 0, 0]

    def __init__(self):

        players = [Player(Goalkeeper(robot_id[0])),
                   Player(Goalkeeper(robot_id[1])),
                   Player(Goalkeeper(robot_id[2]))]

        for robot in range(number_of_robots):
            target = players[robot].getTarget()
            th = players[robot].getTh()
            control_option = players[robot].getControl_Option()

            Team.x[robot] = target[0]
            Team.y[robot] = target[1]
            Team.th[robot] = th
            Team.control_option[robot] = control_option
