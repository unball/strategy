/**
 * @file   goalkeeper_kicker.cpp
 * @author Icaro da Costa Mota
 * @date   25/10/2015
 *
 * @attention Copyright (C) 2015 UnBall Robot Soccer Team
 *
 * @brief
 */

#include <players/goalkeeper_kicker.hpp>

float const GoalkeeperKicker::LEFT_LIMIT = 0.18;
float const GoalkeeperKicker::RIGHT_LIMIT = -0.18;

GoalkeeperKicker::GoalkeeperKicker()
{
	behaviour_ = GOALKEEPER_KICKER;
}

void GoalkeeperKicker::buildPotentialFields(int robot_number)
{
    updateBallPos();
    potential_fields_.push_back(new AttractivePotentialField(ball_pos_, 20));
}

void GoalkeeperKicker::updateBallPos()
{
	Vector ball_pos(Ball::getInstance().getX(),Ball::getInstance().getY());
	ball_pos_ = ball_pos;
}
