
/**
 * @file   assistent_player.cpp
 * @author Icaro da Costa Mota
 * @date   24/10/2015
 *
 * @attention Copyright (C) 2015 UnBall Robot Soccer Team
 *
 * @brief
 */
#include <players/assistent_player.hpp>

float const AssistentPlayer::BALL_RANGE_ = 0.5;

AssistentPlayer::AssistentPlayer()
{
	behaviour_ = ASSISTENT_PLAYER;
	friendly_kicker_ = -1;
}

AssistentPlayer::AssistentPlayer(int friendly_kicker)
{
	behaviour_ = ASSISTENT_PLAYER;
	friendly_kicker_ = friendly_kicker;
}

void AssistentPlayer::buildPotentialFields(int robot_number)
{
    Vector ball_position(Vector(Ball::getInstance().getX(), Ball::getInstance().getY()));
    Vector difference;

    findTarget();

	if (isInBallRange(robot_number))
    {
        potential_fields_.push_back(new SelectivePotentialField(ball_position,
            kick_target_.getDirection(), M_PI/4, 6, false));
    }
    else
    {
        potential_fields_.push_back(new AttractivePotentialField(ball_position, 6));
    }

    avoidTheWalls(robot_number);
}

bool AssistentPlayer::isInBallRange(int robot_number)
{
	Vector ball_position(Vector(Ball::getInstance().getX(), Ball::getInstance().getY()));
    Vector robot_position(robot[robot_number].getX(), robot[robot_number].getY());
    Vector difference = robot_position - ball_position;

    return difference.getMagnitude() < BALL_RANGE_;
}

void AssistentPlayer::findTarget()
{
    kick_target_ = Vector(0,0) - Goals::getInstance().opponent_goal_;
}

void AssistentPlayer::avoidTheWalls(int robot_number)
{
    if (robot[robot_number].getX() > 0.55)
        potential_fields_.push_back(new ParallelPotentialField(Vector(robot[robot_number].getY(), robot[robot_number].getX()),
        Vector(robot[robot_number].getY(), 0.65), 0.2));
    else if (robot[robot_number].getX() < -0.55)
        potential_fields_.push_back(new ParallelPotentialField(Vector(robot[robot_number].getY(), robot[robot_number].getX()),
        Vector(robot[robot_number].getY(), -0.65), 0.2));
    else if (robot[robot_number].getY() > 0.65)
        potential_fields_.push_back(new ParallelPotentialField(Vector(robot[robot_number].getY(), robot[robot_number].getX()),
        Vector(0.75, robot[robot_number].getX()), 0.2));
    else if (robot[robot_number].getY() < -0.65)
        potential_fields_.push_back(new ParallelPotentialField(Vector(robot[robot_number].getY(), robot[robot_number].getX()),
        Vector(-0.75, robot[robot_number].getX()), 0.2));
}
