import rospy
import math
from player import *
from unball.msg import MeasurementSystemMessage
from communication.msg import target_positions_msg
from subprocess import call

start_time = rospy.get_time()
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
        if robot == 0
            msg.x[robot] = xd
            msg.y[robot] = yd
        else
            msg.x[robot] = org_x
            msg.y[robot] = org_y

def start():
    global pub
    rospy.Subscriber('measurement_system_topic',MeasurementSystemMessage,callback)
    rospy.init_node('strategy')
    pub = rospy.Publisher('target_positions_msg', target_positions_msg, queue_size = 10)
    rospy.spin()


if __name__ == '__main__':
    start()
