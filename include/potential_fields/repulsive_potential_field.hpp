/**
 * @file   repulsive_potential_field.hpp
 * @author Matheus Vieira Portela
 * @date   03/08/2015
 *
 * @attention Copyright (C) 2015 UnBall Robot Soccer Team
 *
 * @brief Field that repels the robot from a position.
 */

#ifndef STRATEGY_REPULSIVE_POTENTIAL_FIELD_H_
#define STRATEGY_REPULSIVE_POTENTIAL_FIELD_H_

#include <utils/vector.hpp>
#include <potential_fields/potential_field.hpp>

class RepulsivePotentialField : public PotentialField
{
  public:
    RepulsivePotentialField(Vector origin, float range, float magnitude_weight = 1);
    Vector calculateForce(Vector position);
  
  private:
    Vector origin_;
    float range_;
    float magnitude_weight_;

    bool isInRange(Vector position);
};

#endif  // STRATEGY_REPULSIVE_POTENTIAL_FIELD_H_
