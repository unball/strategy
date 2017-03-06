#!/usr/bin/env python
import rospy
import numpy as np

import potential_fields as pf
from unball.msg import MeasurementSystemMessage
from communication.msg import target_positions_msg
from subprocess import call

BALL_ATTRACTIVE = 4
TANGENCIAL_BALL_MAGNITUDE = 0.5
ENEMY_REPULSIVE_RANGE = 0.7
ENEMY_REPULSIVE_WEIGHT = 1.2
ALLY_REPULSIVE_RANGE = 0.5
ALLY_REPULSIVE_WEIGHT = 0.5
#BALL_ATTRACTIVE =  1.0
#ENEMY_REPULSIVE_RANGE = 0.0
#ENEMY_REPULSIVE_WEIGHT = 0.0
#ALLY_REPULSIVE_RANGE = 0.0
#ALLY_REPULSIVE_WEIGHT = 0.0


number_of_robots = 3
side = 0

def callback(data):
    msg = target_positions_msg()

    #Potential Fields
    attract_ball = pf.AttractivePotentialField(
                        np.array([data.ball_x, data.ball_y]),
                        BALL_ATTRACTIVE, min_magnitude=0.3)
    kick_attract_ball = pf.AttractivePotentialField(
                            np.array([data.ball_x, data.ball_y]),
                            BALL_ATTRACTIVE*2)
    tangencial_ball = pf.TangencialPotentialField(
                        np.array([data.ball_x, data.ball_y]),
                        TANGENCIAL_BALL_MAGNITUDE)
    repulsive_enemy_fields = generate_repulsive_field(data,
                                                      ENEMY_REPULSIVE_RANGE,
                                                      ENEMY_REPULSIVE_WEIGHT,
                                                      ally=False)
    repulsive_ally_fields = generate_repulsive_field(data,
                                                    ALLY_REPULSIVE_RANGE,
                                                    ALLY_REPULSIVE_WEIGHT)



    for robot in range(number_of_robots):
        resultant_vector = np.array([0.0, 0.0])

        #Calculate repulsive force from each enemy
        for field in repulsive_enemy_fields:
            resultant_vector += field.calculate_force(np.array([data.x[robot], data.y[robot]]))

        #Calculate repulsive force from each ally
        for i in range(len(repulsive_ally_fields)):
            #Ignore his own field
            if i != robot:
                resultant_vector += repulsive_ally_fields[i].calculate_force(
                            np.array([data.x[robot], data.y[robot]]))


        #resultant_vector += tangencial_ball.calculate_force(np.array([data.x[robot], data.y[robot]]))
        resultant_vector += attract_ball.calculate_force(np.array([data.x[robot], data.y[robot]]))
        msg.x[robot] = resultant_vector[0]
        msg.y[robot] = resultant_vector[1]

    pub.publish(msg)

#Generate repulsive field for enemies
def generate_repulsive_field(data, range_field, magnitude_weight, ally=True):
    repulsive_fields = []

    if ally == True:
        offset = 0
    else:
        offset = number_of_robots

    for robot in range(number_of_robots):
        field = pf.RepulsivePotentialField(
                                np.array([data.x[robot + offset],
                                        data.y[robot + offset]]),
                                range_field,
                                magnitude_weight)
        repulsive_fields.append(field)

    return repulsive_fields

#def

def start():
    global pub
    pub = rospy.Publisher('target_positions_topic', target_positions_msg, queue_size=10)
    rospy.init_node('strategy')
    rospy.Subscriber('measurement_system_topic', MeasurementSystemMessage, callback)
    rospy.spin()

if __name__ == '__main__':
    start()