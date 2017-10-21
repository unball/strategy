#!/usr/bin/env python
import rospy
from math import *
from measurement_system.msg import measurement_msg
from communication.msg import target_positions_msg
from strategy.msg import strategy_output_msg
from control_options import *

number_of_robots = 3

def callback(data):
    msg = strategy_output_msg()

    if data.x[number_of_robots - 1] < 0.6:
        msg.x[number_of_robots - 1] = 0.7
        msg.y[number_of_robots - 1] = 0

    elif data.y[number_of_robots - 1] > 0.2 or data.y[number_of_robots - 1] < -0.2:
        msg.x[number_of_robots - 1] = 0.7
        msg.y[number_of_robots - 1] = 0

    else:
        msg.x[number_of_robots - 1] = 0.7
        msg.y[number_of_robots - 1] = goalnorm(data)

    msg.control_options[number_of_robots - 1] = control_options.position

    #for robot in range (number_of_robots - 1):
    #    if distance_to_ball(data, robot) > 0.08:
    #        msg.x[robot] = data.ball_x
    #        msg.y[robot] = data.ball_y
    #    else:
    #        msg.x[robot] = -0.75
    #        msg.y[robot] = 0
    #    msg.control_options[robot] = control_options.position

    pub.publish(msg)

def distance_to_ball (a,b):
    distance = sqrt((a.x[b] - a.ball_x)**2 + (a.y[b]- a.ball_y)**2)
    return distance

def goalnorm(data):
    if abs(data.ball_y) < 0.2:
        ball_y = data.ball_y
    elif data.ball_y > 0.2:
        ball_y = 0.2
    else:
        ball_y = -0.2
    return ball_y

def start():
    global pub
    pub = rospy.Publisher('strategy_output_topic', strategy_output_msg, queue_size=10)
    rospy.init_node('strategy')
    rospy.Subscriber('measurement_system_topic', measurement_msg, callback)
    rospy.spin()

if __name__ == '__main__':
    start()
