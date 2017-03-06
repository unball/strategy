#!/usr/bin/env python
import rospy
import numpy as np

import potential_fields as pf
from unball.msg import MeasurementSystemMessage
from communication.msg import target_positions_msg
from subprocess import call

# This script is made to test the tangential potential around the ball.
# If you need to change the behavior of this potential field you can change this constant:
#   * TANGENCIAL_BALL_MAGNITUDE - Indicates the magnitude of field
#
# You can see the potential_fields.py to more informations


TANGENCIAL_BALL_MAGNITUDE = 0.3

number_of_robots = 3

def callback(data):
    msg = target_positions_msg()

    #PCreating an tangential field
    tangencial_ball = pf.TangencialPotentialField(
                        np.array([data.ball_x, data.ball_y]),
                        TANGENCIAL_BALL_MAGNITUDE)

    for robot in range(number_of_robots):

        resultant_vector = tangencial_ball.calculate_force(
                                np.array([data.x[robot], data.y[robot]]))
        msg.x[robot] = resultant_vector[0]
        msg.y[robot] = resultant_vector[1]

    pub.publish(msg)


def start():
    global pub
    pub = rospy.Publisher('target_positions_topic', target_positions_msg, queue_size=10)
    rospy.init_node('strategy')
    rospy.Subscriber('measurement_system_topic', MeasurementSystemMessage, callback)
    rospy.spin()

if __name__ == '__main__':
    start()