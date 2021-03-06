/**
 * @file   goalkeeper_kicker.hpp
 * @author Icaro da Costa Mota
 * @date   25/10/2015
 *
 * @attention Copyright (C) 2015 UnBall Robot Soccer Team
 *
 * @brief
 */

#ifndef STRATEGY_GOALKEEPER_KICKER_H_
#define STRATEGY_GOALKEEPER_KICKER_H_

#include <players/player.hpp>

class GoalkeeperKicker : public Player
{
  public:
  	GoalkeeperKicker();
  	void buildPotentialFields(int robot_number);
  private:
  	void updateBallPos();

  	Vector ball_pos_;

  	static float const LEFT_LIMIT;
  	static float const RIGHT_LIMIT;
};

#endif  // STRATEGY_GOALKEEPER_KICKER_H_
