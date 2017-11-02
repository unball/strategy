#!/usr/bin/env python
import rospy
from measurement_system.msg import measurement_msg
from communication.msg import target_positions_msg
from strategy.msg import strategy_output_msg
from player import *
from ball import *
from team import *

number_of_robots = 3

def callback(data):
    msg = strategy_output_msg()

    Ball.x = data.ball_x
    Ball.y = data.ball_y

    team = Team()

    for robot in range(number_of_robots):
        x = Team.x[robot]
        y = Team.y[robot]
        theta = Team.th[robot]
        control_option = Team.control_option[robot]

        msg.x[robot] = x
        msg.y[robot] = y
        msg.th[robot] = theta
        msg.control_options[robot] = control_option

    pub.publish(msg)

def start():
    global pub
    pub = rospy.Publisher('strategy_output_topic', strategy_output_msg, queue_size=1)
    rospy.init_node('strategy')
    rospy.Subscriber('measurement_system_topic', measurement_msg, callback)
    rospy.spin()

if __name__ == '__main__':
    print "strategy_node started"
    start()
