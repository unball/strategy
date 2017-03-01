/**
 * @file   attractive_potential_field.hpp
 * @author Matheus Vieira Portela
 * @date   03/08/2015
 *
 * @attention Copyright (C) 2015 UnBall Robot Soccer Team
 *
 * @brief Field that attracts the robot to the desired position.
 */

#ifndef STRATEGY_ATTRACTIVE_POTENTIAL_FIELD_H_
#define STRATEGY_ATTRACTIVE_POTENTIAL_FIELD_H_

#include <utils/vector.hpp>
#include <potential_fields/potential_field.hpp>

class AttractivePotentialField : public PotentialField
{
  public:
    AttractivePotentialField(Vector origin, float magnitude);
    Vector calculateForce(Vector position);

  private:
    Vector origin_;
    float magnitude_;

	static float const MIN_MAGNITUDE_;
};

#endif  // STRATEGY_ATTRACTIVE_POTENTIAL_FIELD_H_
