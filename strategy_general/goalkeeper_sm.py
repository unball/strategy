#!/usr/bin/env python
import rospy
import math
from measurement_system.msg import measurement_msg
from communication.msg import target_positions_msg
from strategy.msg import strategy_output_msg
from control_options import *

def states(y_b, y_goalkeeper, state):
    if (y_b > y_goalkeeper) and (y_b < end_y):
        state = 1
    if (y_b < y_goalkeeper) and (y_b > (-1) * end_y):
        state = 2
    if y_b > end_y:
        state = 3
    if y_b < (-1) * end_y:
        state = 4

def state_machine(state, y_b, msg):
    if state == 1:
        msg.y[2] = y_b
        msg.th[2] = math.pi / 2
    if state == 2:
        msg.y[2] = y_b
        msg.th[2] = math.pi / 2
    if state == 3:
        msg.y[2] = end_y
        msg.th[2] = math.pi / 2
    if state == 4:
        msg.y[2] = (-1) * end_y
        msg.th[2] = math.pi / 2

def callback(data):
    msg = strategy_output_msg()

    msg.control_options = [control_options.pose,
                           control_options.pose_line,control_options.pose_line]
    msg.x = [-fixed_x, -fixed_x , fixed_x]

    ball = [data.ball_x, data.ball_y]

    state = 1

    states(ball[1], data.y[2], state)
    state_machine(state, ball[1], msg)

    pub.publish(msg)

def start():
    global pub
    global end_y
    end_y = 0.16
    global fixed_x
    fixed_x = 0.60
    pub = rospy.Publisher('strategy_output_topic', strategy_output_msg, queue_size=10)
    rospy.init_node('strategy')
    rospy.Subscriber('measurement_system_topic', measurement_msg, callback)
    rospy.spin()


if __name__ == '__main__':
    start()
