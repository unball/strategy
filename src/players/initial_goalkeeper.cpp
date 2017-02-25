/**
 * @file   initial_goalkeeper.hpp
 * @author Icaro da Costa Mota
 * @date   22/10/2015
 *
 * @attention Copyright (C) 2015 UnBall Robot Soccer Team
 *
 * @brief
 */

#include <players/initial_goalkeeper.hpp>

float const InitialGoalkeeper::OFFSET = 0.18;

InitialGoalkeeper::InitialGoalkeeper()
{
	behaviour_ = INITIAL_GOALKEEPER;
}

/*void InitialGoalkeeper::buildPotentialFields(int robot_number)
{
	int sign = fabs(Goals::getInstance().friendly_goal_.getY())/Goals::getInstance().friendly_goal_.getY();
	Vector position(Goals::getInstance().friendly_goal_.getX(), Goals::getInstance().friendly_goal_.getY() - sign*OFFSET);
	potential_fields_.push_back(new AttractivePotentialField(position,5));
}*/
