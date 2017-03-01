#!/usr/bin/env python
import rospy
import math
from unball.msg import MeasurementSystemMessage
from communication.msg import target_positions_msg
from subprocess import call

number_of_robots = 3

allies_x = []
allies_y = []
allies_th = []

def receiveGlobalPositions(data):
    del allies_x[:]
    del allies_y[:]
    del allies_th[:]
    for robot in range(number_of_robots):
        allies_x.append(data.x[robot])
        allies_y.append(data.y[robot])
        allies_th.append(data.th[robot])

def convertTargetPositions(global_target):
    msg = target_positions_msg()

    for robot in range(number_of_robots):
        relative_target = [global_target.x[robot] - allies_x[robot], global_target.y[robot] - allies_y[robot]]
        relative_target = convert_axis_to_robot(relative_target, math.radians(allies_th[robot]))

        msg.x[robot] = relative_target[0]
        msg.y[robot] = relative_target[1]

    pub.publish(msg)

#Receive angle in radians
def convert_axis_to_robot(vector, th):
    ax = vector[0]
    ay = vector[1]

    y = ax*math.cos(-th) - ay*math.sin(-th)
    x = ax*math.sin(-th) + ay*math.cos(-th)

    return [x,y]

def start():
    print "teste"
    global pub

    rospy.init_node('relative_position_node')
    pub = rospy.Publisher('relative_positions_topic', target_positions_msg, queue_size=10)
    rospy.Subscriber('measurement_system_topic', MeasurementSystemMessage, receiveGlobalPositions)        
    rospy.Subscriber('target_positions_topic', target_positions_msg, convertTargetPositions)
    rospy.spin()

if __name__ == '__main__':
    start()