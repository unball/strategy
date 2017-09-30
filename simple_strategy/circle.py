import rospy
import math
from measurement_system.msg import measurement_msg
from communication.msg import target_positions_msg

number_of_robots = 3
#Class Circle
w = 1
r = 0.2
org_x = 0
org_y = 0

global start_time

def callback(data):
    msg = target_positions_msg()
    obt_circle(msg)
    pub.publish(msg)

def obt_circle(msg):
    current_time = rospy.get_time() - start_time

    th = w * current_time
    xd = (r * math.cos(th))
    yd = (r * math.sin(th))

    for robot in range(number_of_robots):
        if robot == 0:
            msg.x[robot] = xd
            msg.y[robot] = yd
        elif robot == 1:
            msg.x[robot] = 0.5
            msg.y[robot] = 0.5
        else:
            msg.x[robot] = -0.5
            msg.y[robot] = 0.5

def start():

    global pub
    pub = rospy.Publisher('target_positions_topic', target_positions_msg, queue_size=10)
    rospy.Subscriber('measurement_system_topic', measurement_msg, callback)
    rospy.spin()


if __name__ == '__main__':
    rospy.init_node('strategy')
    start_time = rospy.get_time()
    start()
