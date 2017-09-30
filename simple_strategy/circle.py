import rospy
import math
from player import *
from measurement_system.msg import measurement_msg
from communication.msg import target_positions_msg
from subprocess import call

number_of_robots = 3
#Class Circle
w = 0.1
r = 1
org_x = 0
org_y = 0

def callback(data):
    msg = target_positions_msg()
    obt_circle(msg)
    pub.publish(msg)

def obt_circle(msg):
    current_time = rospy.get_time() - start_time

    th = w * current_time
    xd = (r * cos(th)) + org_x
    yd = (r * sin(th)) + org_y

    for robot in range(number_of_robots):
        if robot == 0:
            msg.x[robot] = xd
            msg.y[robot] = yd
        else:
            msg.x[robot] = org_x
            msg.y[robot] = org_y

def start():

    global pub
    pub = rospy.Publisher('target_positions_topic', target_positions_msg, queue_size=10)
    rospy.init_node('strategy')
    start_time = rospy.get_time()
    rospy.Subscriber('measurement_system_topic', measurement_msg, callback)
    rospy.spin()


if __name__ == '__main__':
    start()
