#!/usr/bin/env python
import rospy
from std_msgs.msg import Char

def start():
    rospy.init_node('keyboard_event')
    pub = rospy.Publisher('keyboard_event_topic', Char, queue_size=1)
    rate = rospy.Rate(10)
    keyboard_event = Char()

    while not rospy.is_shutdown():
        keyboard_event.data = input()
        pub.publish(keyboard_event)

if __name__ == '__main__':
    print "keyboard_event publisher"
    start()
