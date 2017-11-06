#!/usr/bin/env python
import rospy
from measurement_system.msg import measurement_msg
from communication.msg import target_positions_msg
from strategy.msg import KeyboardMessage
from strategy.msg import strategy_output_msg
from player import *
from team import *
from std_msgs.msg import String
from field_side import *
from point import Point

number_of_robots = 3
paused = False

def callback(data, team):
    ball = Point(data.ball_x, data.ball_y)
    team.set_params(ball, data.x, data.y, data.th)

def assembly_msg(output):
    aux = strategy_output_msg()
    for i in xrange(len(output)):
        aux.x[i] = output[i][0]
        aux.y[i] = output[i][1]
        aux.th[i] = output[i][2]
        aux.u[i] = output[i][3]
        aux.w[i] = output[i][4]
        aux.vx[i] = output[i][5]
        aux.vy[i] = output[i][6]
        aux.control_options[i] = output[i][7]
    return aux

def keyboardListener(data):
    global paused
    if data.key == 112:
        paused = True
    if data.key == 114:
        paused = False

def fieldSideListener(field_side):
    if (field_side.data == "Right"):
        FieldSide.side = Side.RIGHT
    elif (field_side.data == "Left"):
        FieldSide.side = Side.LEFT

def start(team):
    global output_msg
    pub = rospy.Publisher('strategy_output_topic', strategy_output_msg, queue_size=1)
    rospy.init_node('strategy')
    rospy.Subscriber('measurement_system_topic', measurement_msg, callback, team)
    rospy.Subscriber('keyboard_topic', KeyboardMessage, keyboardListener)
    rospy.Subscriber('field_side_topic', String, fieldSideListener)
    rate = rospy.Rate(30)
    output_msg = strategy_output_msg()
    try:
        while not rospy.is_shutdown():
            if (paused == False):
                team.run()
            else:
                team.stop()
            output = team.output()
            output_msg = assembly_msg(output)
            pub.publish(output_msg)
            rate.sleep()
    except rospy.ROSInterruptException:
        exit(1)


if __name__ == '__main__':
    print "strategy_node started"
    team = Team()
    start(team)
