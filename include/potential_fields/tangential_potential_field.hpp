/**
 * @file   tangential_potential_field.hpp
 * @author Izabella Thais Oliveira Gomes
 * @date   29/07/2015
 *
 * @attention Copyright (C) 2015 UnBall Robot Soccer Team
 *
 * @brief Potential field that affects objects to be oriented
 * around to the origin according to the distance to its
 * origin.
 */

#ifndef STRATEGY_TANGENTIAL_POTENTIAL_FIELD_H_
#define STRATEGY_TANGENTIAL_POTENTIAL_FIELD_H_

#include <utils/vector.hpp>
#include <potential_fields/potential_field.hpp>

class TangentialPotentialField : public PotentialField
{
  public:
    TangentialPotentialField(Vector origin, float magnitude);
    Vector calculateForce(Vector position);
  
  private:
    Vector origin_;
    float magnitude_;
};

#endif  // STRATEGY_TANGENTIAL_POTENTIAL_FIELD_H_