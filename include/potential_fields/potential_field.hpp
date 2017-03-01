/**
 * @file   potential_field.hpp
 * @author Matheus Vieira Portela
 * @date   27/06/2015
 *
 * @attention Copyright (C) 2015 UnBall Robot Soccer Team
 *
 * @brief Abstract potential field.
 */

#ifndef STRATEGY_POTENTIAL_FIELD_H_
#define STRATEGY_POTENTIAL_FIELD_H_

#include <utils/vector.hpp>

class PotentialField
{
  public:
    virtual Vector calculateForce(Vector position) = 0;
};

#endif  // STRATEGY_POTENTIAL_FIELD_H_
