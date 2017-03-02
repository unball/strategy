/**
 * @file   parallel_potential_field.hpp
 * @author Izabella Thais Oliveira Gomes
 * @date   27/07/2015
 *
 * @attention Copyright (C) 2015 UnBall Robot Soccer Team
 *
 * @brief Potential field that affects objects to be oriented parallel
 * to the origin according to the distance to its origin.
 */

#ifndef STRATEGY_PARALLEL_POTENTIAL_FIELD_H_
#define STRATEGY_PARALLEL_POTENTIAL_FIELD_H_

#include <utils/vector.hpp>
#include <potential_fields/potential_field.hpp>

class ParallelPotentialField : public PotentialField
{
  public:
    ParallelPotentialField(Vector origin, Vector field_force, float max_distance);
    Vector calculateForce(Vector position);
  
  private:
    Vector origin_;
    Vector field_force_;
    float max_distance_;
};

#endif  // STRATEGY_PARALLEL_POTENTIAL_FIELD_H_