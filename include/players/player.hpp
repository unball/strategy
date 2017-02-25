/**
 * @file   player.hpp
 * @author Icaro da Costa Mota
 * @date   08/09/2015
 *
 * @attention Copyright (C) 2015 UnBall Robot Soccer Team
 *
 * @brief
 */

#ifndef STRATEGY_PLAYER_H_
#define SRATEGY_PLAYER_H_

#include <memory>

#include <utils/vector.hpp>

#include <ball.hpp>
#include <robot.hpp>
#include <goals.hpp>
/*#include <attractive_potential_field.hpp>
#include <parallel_potential_field.hpp>
#include <perpendicular_potential_field.hpp>
#include <repulsive_potential_field.hpp>
#include <selective_potential_field.hpp>
#include <tangential_potential_field.hpp>
*/
enum player_behaviour
{
    INITIAL_GOALKEEPER,
    GOALKEEPER,
    GOALKEEPER_KICKER,
    REGULAR_PLAYER,
    ASSISTENT_PLAYER,
    KICKER_PLAYER
};

class Player
{
  public:
  	//~Player();
  	//virtual void buildPotentialFields(int robot_number) = 0;
  	//void clearPotentialFields();
  	//Vector calculateResultantForce(int robot_number);

  	player_behaviour getBehaviour();
  protected:
  	//std::vector<PotentialField*> potential_fields_;

  	player_behaviour behaviour_;
};

#endif  // STRATEGY_PLAYER_H_