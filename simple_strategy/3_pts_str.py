import rospy
import math
from measurement_system.msg import measurement_msg
from communication.msg import target_positions_msg

number_of_robots = 3

global position = 0.5

def set_3_pnts(msg):
    for robot in range(number_of_robots):
        msg.x[robot] = position
        msg.y[robot] = position


def callback(data):
    msg = target_positions_msg()
    set_3_pnts(msg)
    pub.publish(msg)
    rospy.sleep(3.)
    position = -1 * position


def start():

    global pub
    pub = rospy.Publisher('target_positions_topic', target_positions_msg, queue_size=10)
    rospy.Subscriber('measurement_system_topic', measurement_msg, callback)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('strategy')
    start()
