#!/usr/bin/env python
import rospy
import math
from measurement_system.msg import measurement_msg
from communication.msg import target_positions_msg
from strategy.msg import strategy_output_msg
from control_options import *

number_of_robots = 3

def callback(data):
    msg = target_positions_msg()
    msg2 = strategy_output_msg()
    ball = [data.ball_x, data.ball_y]

    for robot in range(number_of_robots):
        msg.x[robot] = data.ball_x
        msg.y[robot] = data.ball_y
        msg2.x[robot] = data.ball_x
        msg2.y[robot] = data.ball_y
        msg2.control_options[robot] = control_options.position

    pub.publish(msg)
    pub2.publish(msg2)


def start():
    global pub
    global pub2
    pub = rospy.Publisher('target_positions_topic', target_positions_msg, queue_size=10)
    pub2 = rospy.Publisher('strategy_output_topic', strategy_output_msg, queue_size=10)
    rospy.init_node('strategy')
    rospy.Subscriber('measurement_system_topic', measurement_msg, callback)
    rospy.spin()

if __name__ == '__main__':
    start()
