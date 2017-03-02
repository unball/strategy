#!/usr/bin/env python
import rospy
import math
from unball.msg import MeasurementSystemMessage
from communication.msg import target_positions_msg
from subprocess import call

our_field_side = 'left'

def main():
    global pub
    rospy.init_node('goalkeeper')
    pub = rospy.Publisher('target_positions_topic', target_positions_msg, queue_size=10)
    rospy.Subscriber('measurement_system_topic', MeasurementSystemMessage, callback)
    rospy.spin()

def callback(data):
    msg = target_positions_msg()
    goalkeeperObjective = calculateGoalkeeperObjective([data.ball_x, data.ball_y])
    msg.x[0] = goalkeeperObjective[0]
    msg.y[0] = goalkeeperObjective[1]

    # Make other robots stay in position
    for i in [1, 2]:
        msg.x[i] = data.x[i]
        msg.y[i] = data.y[i]
    pub.publish(msg)

def calculateGoalkeeperObjective(ball_pos):
    objective = [0, 0]
    objective[0] = 0.65
    if our_field_side == 'left':
        objective[1] = ball_pos[1]
    if objective[1] > 0.13:
        objective[1] = 0.13
    if objective[1] < -0.13:
        objective[1] = -0.13
    return objective


if __name__ == '__main__':
    main()
