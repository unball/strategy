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
        K_ball = 13

        robot = np.array([self.allies[self.my_index][0], self.allies[self.my_index][1]])

        opponent_goal = self.get_opponent_goal()

        goal_to_ball = opponent_goal - self.ball
        goal_to_ball_mag = pf.cart2polar(goal_to_ball)[0]
        goal_to_ball_angle = pf.cart2polar(goal_to_ball)[1]

        goal_to_robot = opponent_goal - robot
        goal_to_robot_mag = pf.cart2polar(goal_to_robot)[0]
        goal_to_robot_angle = pf.cart2polar(goal_to_robot)[1]

        robot_to_ball = self.ball - robot
        robot_to_ball_mag = pf.cart2polar(robot_to_ball)[0]

        if((np.fabs(goal_to_ball_angle - goal_to_robot_angle) <= np.pi/6)
                    and is_on_attack_mode(robot[0], self.ball[0])
                    and (robot_to_ball_mag <= 0.07)):
            target = opponent_goal
            print ' gol de placa'
        else:
            target = (self.ball - goal_to_ball/K_ball)
            #target[1] += 0.3
            print 'preparando'

        return target

    def get_opponent_goal(self):
        global side_opponent
        side_opponent = 'Left' if self.field_side == 'Right' else 'Right'
        print side_opponent
        if(side_opponent == 'Right'):
            return np.array([0.8, 0])
        else:
            return np.array([-0.8, 0])
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
       return x_robot < x_ball
    else:
        return x_robot > x_ball

def start():
    global pub
    pub = rospy.Publisher('target_positions_topic', target_positions_msg, queue_size=10)
    rospy.init_node('strategy')
    rospy.Subscriber('measurement_system_topic', MeasurementSystemMessage, callback)
    rospy.spin()

if __name__ == '__main__':
    start()