#!/usr/bin/env python
import rospy
import math
from unball.msg import MeasurementSystemMessage
from communication.msg import target_positions_msg
from subprocess import call

number_of_robots = 3

def callback(data):
    msg = target_positions_msg()

    for robot in range(number_of_robots):
        target = [data.ball_x, data.ball_y]

        msg.x[robot] = target[0]
        msg.y[robot] = target[1]

    pub.publish(msg)


def start():
    global pub
    pub = rospy.Publisher('target_positions_topic', target_positions_msg, queue_size=10)
    rospy.init_node('strategy')
    rospy.Subscriber('measurement_system_topic', MeasurementSystemMessage, callback)
    rospy.spin()

if __name__ == '__main__':
    start()