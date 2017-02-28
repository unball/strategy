#!/usr/bin/env python
import rospy
import math
from unball.msg import MeasurementSystemMessage
from communication.msg import target_positions_msg
from subprocess import call


number_of_robots = 3

def normalize_vector(vector):
    ax = vector[0]
    ay = vector[1]
    mag = math.sqrt(ax*ax + ay*ay)


    if(mag != 0):
        return [ax/mag, ay/mag]
    else:
        return [0,0]

#Receive angle in radians
def convert_axis_to_robot(vector, th):
    ax = vector[0]
    ay = vector[1]

    y = ax*math.cos(-th) - ay*math.sin(-th)
    x = ax*math.sin(-th) + ay*math.cos(-th)

    return [x,y]


def callback(data):
    msg = target_positions_msg()
    allies_x = []
    allies_y = []
    allies_th = []
    target_vector = []

    ball_x = data.ball_x
    ball_y = data.ball_y


    for robot in range(number_of_robots):
        allies_x.append(data.x[robot])
        allies_y.append(data.y[robot])
        allies_th.append(data.th[robot])

        target = [ball_x - allies_x[robot], ball_y - allies_y[robot]]
        target = convert_axis_to_robot(target, math.radians(allies_th[robot]))
        target_vector.append(target)
        #target_vector.append(normalize_vector(target))

        msg.x[robot] = target_vector[robot][0]
        msg.y[robot] = target_vector[robot][1]

    pub.publish(msg)


def start():
        global pub
        pub = rospy.Publisher('target_positions_topic', target_positions_msg, queue_size=10)
        rospy.init_node('strategy')
        rospy.Subscriber('measurement_system_topic', MeasurementSystemMessage, callback)
        rospy.spin()

if __name__ == '__main__':
    start()