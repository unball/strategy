/**
 * @file   goals.hpp
 * @author Icaro da Costa Mota
 * @date   23/10/2015
 *
 * @attention Copyright (C) 2015 UnBall Robot Soccer Team
 *
 * @brief
 */

#ifndef STRATEGY_GOALS_H_
#define STRATEGY_GOALS_H_

#include <ros/ros.h>
#include <cmath>

#include <utils/vector.hpp>
#include <robot.hpp>
#include <ball.hpp>

class Goals
{
  public:
    static Goals& getInstance();

  	Vector friendly_goal_;
    Vector opponent_goal_;

	void setGoalkeeperSide(float x);
	int findOpponentGoalkeeper();
	bool isBallInFriendlyGoalArea();
  private:
    static Goals *instance;
};

#endif  // STRATEGY_GOALS_H_