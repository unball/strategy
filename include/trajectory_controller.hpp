/**
 * @file   trajectory_controller.hpp
 * @author Matheus Vieira Portela
 * @date   03/08/2015
 *
 * @attention Copyright (C) 2015 UnBall Robot Soccer Team
 *
 * @brief Control robots trajectory by applying potential fields.
 */

#ifndef STRATEGY_TRAJECTORY_CONTROLLER_H_
#define STRATEGY_TRAJECTORY_CONTROLLER_H_

#include <memory>

#include <utils/vector.hpp>
#include <ball.hpp>
#include <robot.hpp>
/*#include <players/regular_player.hpp>
#include <players/goalkeeper.hpp>
#include <players/goalkeeper_kicker.hpp>
#include <players/initial_goalkeeper.hpp>
#include <players/kicker_player.hpp>
#include <players/assistent_player.hpp>*/

class TrajectoryController
{
  public:
    TrajectoryController();
    //~TrajectoryController();
    //void run();
    void initialPosition();
    void stopRobot(int robot_number);

    //void updatePlayer(int robot_number, player_behaviour behaviour);

    //Player* getPlayer(int robot_number);
  private:
    //Player* player_[3];

    //std::vector<PotentialField*> potential_fields_;
    float angle_error_prev_;

    // Holds whether the robot moves with direct or inverse motion.
    bool direct_motion_;

    //void controlRobot(int robot_number, Vector force);
    //void turn(int robot_number, float angle);
    //void move(int robot_number, float distance);

    bool isInBallRange(int robot_number);
};

#endif  // STRATEGY_TRAJECTORY_CONTROLLER_H_