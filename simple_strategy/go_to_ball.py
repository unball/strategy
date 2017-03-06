#!/usr/bin/env python
import rospy
import math
from player import *
from unball.msg import MeasurementSystemMessage
from communication.msg import target_positions_msg
from subprocess import call

number_of_robots = 3

ball = []

class Go_To_Ball(Player):
    def getTarget(self):
        return self.ball

player = [Go_To_Ball(), Go_To_Ball(), Go_To_Ball()]

def callback(data):
    msg = target_positions_msg()
    ball = [data.ball_x, data.ball_y]

    for robot in range(number_of_robots):
        player[robot].setPositions(ball = ball)
        target = player[robot].getTarget()

        msg.x[robot] = target[0]
        msg.y[robot] = target[1]

    pub.publish(msg)


def start():
    global pub
    pub = rospy.Publisher('target_positions_topic', target_positions_msg, queue_size=10)
    rospy.init_node('strategy')
    rospy.Subscriber('measurement_system_topic', MeasurementSystemMessage, callback)
    rospy.spin()

if __name__ == '__main__':
    start()