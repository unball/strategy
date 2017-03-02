/**
 * @file   initial_goalkeeper.hpp
 * @author Icaro da Costa Mota
 * @date   22/10/2015
 *
 * @attention Copyright (C) 2015 UnBall Robot Soccer Team
 *
 * @brief
 */

#ifndef STRATEGY_INITIAL_GOALKEEPER_H_
#define STRATEGY_INITIAL_GOALKEEPER_H_

#include <players/player.hpp>
#include <goals.hpp>

class InitialGoalkeeper : public Player
{
  public:
  	InitialGoalkeeper();
  	void buildPotentialFields(int robot_number);
  private:
  	static float const OFFSET;
};

#endif  // STRATEGY_INITIAL_GOALKEEPER_H_
