#!/usr/bin/env python
import rospy
from math import *
from measurement_system.msg import measurement_msg
from communication.msg import target_positions_msg
from strategy.msg import strategy_output_msg
from control_options import *


def callback(data):
    msg = strategy_output_msg()

    msg.control_options = [control_options.pose,
                           control_options.pose, control_options.pose]

    msg.x[0] = -0.5
    msg.y[0] = 0.5
    msg.th[0] = pi / 2

    msg.x[1] = 0
    msg.y[1] = 0.5
    msg.th[1] = pi

    msg.x[2] = 0.5
    msg.y[2] = 0.5
    msg.th[2] = pi * (3. / 2)

    pub.publish(msg)


def start():
    global pub
    pub = rospy.Publisher('strategy_output_topic',
                          strategy_output_msg, queue_size=10)
    rospy.init_node('strategy')
    rospy.Subscriber('measurement_system_topic', measurement_msg, callback)
    rospy.spin()


if __name__ == '__main__':
    start()
