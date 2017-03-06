#!/usr/bin/env python
import rospy
import numpy as np
from player import *
import potential_fields as pf
from unball.msg import MeasurementSystemMessage
from communication.msg import target_positions_msg
from subprocess import call

side_opponent = 'Right'
number_of_robots = 1

ball = []
allies = [ [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]

class Kicker(Player):
    def getTarget(self):
        K_ball = 20.0

        robot = np.array([self.allies[self.my_index][0], self.allies[self.my_index][1]])

        if(side_opponent == 'Right'):
            opponent_goal =  np.array([0.8, 0])
        else:
            opponent_goal =  np.array([-0.8, 0])

        goal_to_ball = opponent_goal - self.ball
        goal_to_ball[1] = -goal_to_ball[1]
        goal_to_ball_angle = pf.cart2polar(goal_to_ball)[1]
        goal_to_ball_mag = pf.cart2polar(goal_to_ball)[0]

        goal_to_robot = opponent_goal - robot
        goal_to_robot_angle = pf.cart2polar(goal_to_robot)[1]
        goal_to_robot_mag = pf.cart2polar(goal_to_robot)[0]

        robot_to_ball = robot - self.ball
        robot_to_ball_mag = pf.cart2polar(robot_to_ball)[0]

        if((np.fabs(goal_to_ball_angle - goal_to_robot_angle) <= np.pi/15)
            and (robot_to_ball_mag <= 0.1)
            and is_on_attack_mode(robot[0], self.ball[0])):
        #):
            target = opponent_goal
            target[0] = -target[0]
            print ' gol de placa'
        else:
            target = (self.ball + goal_to_robot/K_ball)
            print ' preparando'

        return target

player = Kicker()

def callback(data):
    msg = target_positions_msg()

    ball = [data.ball_x, data.ball_y]
    for i in range(3):
        allies[i] = [data.x[i], data.y[i], data.th[i]]

    for robot in range(number_of_robots):
        player.setPositions(ball = ball, allies = allies, my_index = robot)
        target = player.getTarget()

        msg.x[robot] = target[0]
        msg.y[robot] = target[1]

    pub.publish(msg)


def is_on_attack_mode(x_robot, x_ball):
    if(side_opponent == 'Right'):
       return x_robot > x_ball
    else:
        return x_robot < x_ball

def start():
    global pub
    pub = rospy.Publisher('target_positions_topic', target_positions_msg, queue_size=10)
    rospy.init_node('strategy')
    rospy.Subscriber('measurement_system_topic', MeasurementSystemMessage, callback)
    rospy.spin()

if __name__ == '__main__':
    start()