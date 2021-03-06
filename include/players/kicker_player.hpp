
/**
 * @file   kicker_player.hpp
 * @author Izabella Thais Oliveira Gomes
 * @date   22/10/2015
 *
 * @attention Copyright (C) 2015 UnBall Robot Soccer Team
 *
 * @brief
 */

#ifndef STRATEGY_KICKER_PLAYER_H_
#define STRATEGY_KICKER_PLAYER_H_

#include <players/player.hpp>

class KickerPlayer : public Player
{
  public:
  	KickerPlayer();
  	void buildPotentialFields(int robot_number);

  private:
  	void findTarget();

  	static float const BALL_RANGE_;

  	bool isInBallRange(int robot_number);
  	bool opponentGoalkeeperIsInGoalRange(int opponent_goalkeeper);
    void avoidTheWalls(int robot_number);

  	float target_;
  	Vector kick_target_;
};

#endif  // STRATEGY_KICKER_PLAYER_H_
