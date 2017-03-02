
/**
 * @file   regular_player.hpp
 * @author Icaro da Costa Mota
 * @date   08/09/2015
 *
 * @attention Copyright (C) 2015 UnBall Robot Soccer Team
 *
 * @brief
 */

#ifndef STRATEGY_REGULAR_PLAYER_H_
#define STRATEGY_REGULAR_PLAYER_H_

#include <players/player.hpp>

class RegularPlayer : public Player
{
  public:
  	RegularPlayer();
  	void buildPotentialFields(int robot_number);
  	bool isInBallRange(int robot_number);

  private:
  	void avoidTheWalls(int robot_number);

  	static float const BALL_RANGE_;
};

#endif  // STRATEGY_REGULAR_PLAYER_H_
