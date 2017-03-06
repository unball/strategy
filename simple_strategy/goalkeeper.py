#!/usr/bin/env python
import rospy
import math
from player import *
from unball.msg import MeasurementSystemMessage
from communication.msg import target_positions_msg
from subprocess import call

our_field_side = 'left'
goal_area_x_position = 0.68
goal_area_max_y = 0.17


allies = [[], [], []]
ball = []

class Goalkeeper(Player):
    def getTarget(self):
        objective = [0, 0]
        objective[0] = goal_area_x_position
        if our_field_side == 'left':
            objective[0] *= -1
        objective[1] = clamp(self.ball[1], -goal_area_max_y, goal_area_max_y)
        return objective

player = Goalkeeper()

def main():
    global pub
    rospy.init_node('goalkeeper')
    pub = rospy.Publisher('target_positions_topic', target_positions_msg, queue_size=10)
    rospy.Subscriber('measurement_system_topic', MeasurementSystemMessage, callback)
    rospy.spin()

def callback(data):
    msg = target_positions_msg()

    ball = [data.ball_x, data.ball_y]
    for robot in range(3):
        allies[robot] = [data.x[robot], data.y[robot]]

    player.setPositions(allies = allies, ball = ball)

    msg.x[0], msg.y[0] = player.getTarget() 

    # Make other robots stay in position
    for i in [1, 2]:
        msg.x[i] = data.x[i]
        msg.y[i] = data.y[i]

    pub.publish(msg)

def clamp(value, min, max):
    if value > max:
        value = max
    if value < min:
        value = min
    return value

if __name__ == '__main__':
    main()
