#!/usr/bin/env python
import rospy
import math
from std_msgs.msg import String
from player import *
from unball.msg import MeasurementSystemMessage
from communication.msg import target_positions_msg
from subprocess import call

goal_area_x_position = 0.68
goal_area_max_y = 0.17

class Goalkeeper(Player):
    def getTarget(self):
        objective = [0, 0]
        objective[0] = goal_area_x_position
        if self.field_side == 'Left':
            objective[0] *= -1
        objective[1] = clamp(self.ball[1], -goal_area_max_y, goal_area_max_y)
        return objective

player = Goalkeeper()

def main():
    global pub
    global field_side
    field_side = 'Left'
    rospy.init_node('goalkeeper')
    pub = rospy.Publisher('target_positions_topic', target_positions_msg, queue_size=10)
    rospy.Subscriber('measurement_system_topic', MeasurementSystemMessage, measurement_callback)
    rospy.Subscriber('field_side_topic', String, field_side_callback)
    rospy.spin()

def measurement_callback(data):
    msg = target_positions_msg()

    ball = [data.ball_x, data.ball_y]
    allies = [[], [], []]
    for robot in range(3):
        allies[robot] = [data.x[robot], data.y[robot]]

    player.setPositions(allies = allies, ball = ball, field_side = field_side)

    for i in range(3):
        msg.x[i], msg.y[i] = player.getTarget()

    pub.publish(msg)

def field_side_callback(data):
    global field_side
    field_side = data.data

# TODO: put this in another script
def clamp(value, min, max):
    if value > max:
        value = max
    if value < min:
        value = min
    return value

if __name__ == '__main__':
    main()
