import rospy
import math
from measurement_system.msg import measurement_msg
from communication.msg import target_positions_msg

global k
k = 1

def set_3_pnts(msg, k):
    msg.y[0] = 0.5 * k
    msg.x[0] = 0.5

    msg.y[1] = 0.5 * k
    msg.x[1] = 0

    msg.y[2] = 0.5 * k
    msg.x[2] = -0.5

def callback(data):
    msg = target_positions_msg()
    set_3_pnts(msg)
    pub.publish(msg)
    rospy.sleep(3.)
    k = k * -1


def start():

    global pub
    pub = rospy.Publisher('target_positions_topic', target_positions_msg, queue_size=10)
    rospy.Subscriber('measurement_system_topic', measurement_msg, callback)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('strategy')
    start()
