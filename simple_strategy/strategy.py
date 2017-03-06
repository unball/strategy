#!/usr/bin/env python
from goalkeeper import *
from go_to_ball import *
from kicker import *

number_of_robots = 2

allies = [[], [], []]
ball = []

players = [Kicker(), Goalkeeper()]

def callback(data):
    msg = target_positions_msg()

    ball = [data.ball_x, data.ball_y]

    for robot in range(number_of_robots):
        allies[robot] = [data.x[robot], data.y[robot]]

    for robot in range(number_of_robots):
        players[robot].setPositions(allies = allies, ball = ball, my_index = robot)
        msg.x[robot], msg.y[robot] = players[robot].getTarget()

    pub.publish(msg)

def start():
    global pub
    pub = rospy.Publisher('target_positions_topic', target_positions_msg, queue_size=10)
    rospy.init_node('strategy')
    rospy.Subscriber('measurement_system_topic', MeasurementSystemMessage, callback)
    rospy.spin()

if __name__ == '__main__':
    start()