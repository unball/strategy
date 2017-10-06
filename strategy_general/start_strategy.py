#!/usr/bin/env python
import rospy
import math
from measurement_system.msg import measurement_msg
from communication.msg import target_positions_msg
from strategy.msg import strategy_output_msg


def callback(data):
    msg = target_positions_msg()
    msg2 = strategy_output_msg()
    msg.x[0]=2
    msg2.x[0]=3
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
