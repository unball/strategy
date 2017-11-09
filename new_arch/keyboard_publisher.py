#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def start():
    rospy.init_node('keyboard_event')
    pub = rospy.Publisher('keyboard_topic', String, queue_size=1)
    rate = rospy.Rate(10)
    keyboard_event = String()

    while not rospy.is_shutdown():
        keyboard_event.data = raw_input()
        pub.publish(keyboard_event)

if __name__ == '__main__':
    print "keyboard_event publisher started"
    start()
