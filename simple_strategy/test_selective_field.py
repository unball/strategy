#!/usr/bin/env python
import rospy
import numpy as np

import potential_fields as pf
from unball.msg import MeasurementSystemMessage
from communication.msg import target_positions_msg
from subprocess import call

# This script is made to test the attractive potential towards the ball.
# If you need to change the behavior of this potential field you can change some constants:
#   * BALL_ATTRACTIVE - Indicates the magnitude of field
#   * min_magnitude - Indicates the distance thats the field act constantly
#
# You can see the potential_fields.py to more informations

SELECTIVE_WIDTH = np.pi/4
SELECTIVE_RANGE = 1

side_opponent = 'Right'
number_of_robots = 1

def callback(data):
    msg = target_positions_msg()

    if(side_opponent == 'Right'):
        opponent_goal =  np.array([0.8, 0])
    else:
        opponent_goal =  np.array([-0.8, 0])
    direction = np.array([data.ball_x, data.ball_y]) - opponent_goal

    #Creating attractive potential
    selective_field = pf.SelectivePotentialField(
                        np.array([data.ball_x, data.ball_y]),
                        SELECTIVE_WIDTH, SELECTIVE_RANGE, direction, opponent_goal, 4, 0.3)

    for robot in range(number_of_robots):
        resultant_vector = selective_field.calculate_force(np.array([data.x[robot], data.y[robot]]))
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