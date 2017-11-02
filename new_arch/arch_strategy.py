#!/usr/bin/env python
import rospy
from measurement_system.msg import measurement_msg
from communication.msg import target_positions_msg
from strategy.msg import strategy_output_msg
from player import *
from point import Point
from team import *

number_of_robots = 3
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
def start(team):
    global output_msg
    pub = rospy.Publisher('strategy_output_topic', strategy_output_msg, queue_size=1)
    rospy.init_node('strategy')
    rospy.Subscriber('measurement_system_topic', measurement_msg, callback, team)
    rate = rospy.Rate(30)
    output_msg = strategy_output_msg()
    try:
        while not rospy.is_shutdown():
            team.run()
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
