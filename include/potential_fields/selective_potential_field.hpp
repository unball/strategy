/**
 * @file   selective_potential_field.hpp
 * @author Izabella Thais Oliveira Gomes
 * @date   29/07/2015
 *
 * @attention Copyright (C) 2015 UnBall Robot Soccer Team
 *
 * @brief Potential field that affects objects according to the distance to its
 * origin in a particular area and with a specific width. It consist of a junction
 * of the radial and tangencial field, but with some particularities.
 */

#ifndef STRATEGY_SELECTIVE_POTENTIAL_FIELD_H_
#define SRATEGY_SELECTIVE_POTENTIAL_FIELD_H_

#include <utils/vector.hpp>
#include <utils/math.hpp>
#include <potential_fields/potential_field.hpp>
#include <potential_fields/repulsive_potential_field.hpp>

class SelectivePotentialField : public PotentialField
{
  public:
    SelectivePotentialField(Vector origin, float direction, float width, float range, bool isSmooth = true);
    Vector calculateForce(Vector robot_position);

  private:
    // The position attracting robots.
    Vector origin_;

    // The direction, in radians, of the field normal vector.
    float direction_;

    // The width, in radians, this field has.
    float width_;

    // The magnitude of the force applied to the robots.
    float range_;

    bool isSmooth_;

    bool isInTheCone(Vector difference, float weight = 1);
    Vector applyAttractivePotentialField(Vector difference);
    Vector applyTangentialField(Vector difference);
    float rotateClockwise(float angle);
    float rotateCounterClockwise(float angle);

    bool shouldRotateClockwise(int angle_quadrant, int direction_quadrant, float resultant_angle);

    static float const MIN_MAGNITUDE_;
    //HACK: We added this const to stop the robot from overshooting when going around the target.
    static float const TANGENTIAL_CORRECTION_;
};

#endif  // STRATEGY_SELECTIVE_POTENTIAL_FIELD_H_
