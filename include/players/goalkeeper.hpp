/**
 * @file   goalkeeper.hpp
 * @author Icaro da Costa Mota
 * @date   08/09/2015
 *
 * @attention Copyright (C) 2015 UnBall Robot Soccer Team
 *
 * @brief
 */

#ifndef STRATEGY_GOALKEEPER_H_
#define STRATEGY_GOALKEEPER_H_

#include <players/player.hpp>
#include <goals.hpp>

class Goalkeeper : public Player
{
  public:
  	Goalkeeper();
  	void buildPotentialFields(int robot_number);
  private:
  	void stayAtTheBoundary();
  	bool isBallInRange();
  	void goToTheBoundary(float limit);

  	void updateBallPos();

    float y_pos_;
  	Vector ball_pos_;

  	static float const LEFT_LIMIT;
  	static float const RIGHT_LIMIT;
};

#endif  // STRATEGY_GOALKEEPER_H_
