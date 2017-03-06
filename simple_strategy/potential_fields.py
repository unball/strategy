#!/usr/bin/env python
import numpy as np

#Convert vector from cartesian to polar coordinate
#@vector = [x, y]
def cart2polar(vector):
    x = vector[0]
    y = vector[1]
    r = np.sqrt(x*x + y*y)
    th = np.arctan2(y, x)
    return np.array([r, th])

#Convert vector from polar to cartesian coordinate
#@vector = [r, th]
def polar2cart(vector):
    r = vector[0]
    th = vector[1]
    x = r*np.cos(th)
    y = r*np.sin(th)
    return np.array([x,y])

class AttractivePotentialField:
    """Radial attractive potential field
        @origin Point that starts the field - Cartesian coordinates
        @magnitude Radius of field """
    def __init__(self, origin, magnitude, min_magnitude=1):
        self.origin = origin
        self.magnitude = magnitude
        self.min_magnitude = min_magnitude

    def calculate_force(self, position):
        return self.origin
        #difference = difference*np.array([self.magnitude, 1])

        #if(difference[0] < self.min_magnitude):
        #    difference[0] = self.min_magnitude

class RepulsivePotentialField:
    """Radial repulsive potential field
        @origin Point that starts the field - Cartesian coordinates
        @range_field Distance from origin that fields act
        @magnitude_weight Weight that fields act"""
    def __init__(self, origin, range_field, magnitude_weight):
        self.origin = origin
        self.range_field = range_field
        self.magnitude_weight = magnitude_weight

    def calculate_force(self, position):
        difference = cart2polar(position - self.origin)

        if(difference[0] < self.range_field):
            difference[0] = (self.range_field - difference[0])/(self.range_field/self.magnitude_weight)

        else:
            difference = np.array([0,0])

        return polar2cart(difference)

class TangencialPotentialField:
    """Tangencial potential field
        @origin Point that starts the field - Cartesian coordinates
    """
    def __init__(self, origin, magnitude):
        self.origin = origin
        self.magnitude = magnitude

    def calculate_force(self, position):
        difference = cart2polar(self.origin - position)
        difference[0] = self.magnitude
        difference[1] += np.pi/2.5
        print difference[1]

        return polar2cart(difference)

class SelectivePotentialField:
    """Selective Potential field
    set a combination of fields thats allows to kick the ball inside
    of a conic region
        @origin Point that starts the field - Cartesian coordinates
        @direction Vector that indicates the direction
        @magnitude
    x"""

    def __init__(self, origin, width, range_field, direction, goal,
                mag_attractive_field, mag_tangencial_field):
        self.origin = origin
        self.width = width
        self.range_field = range_field
        self.direction = direction
        self.mag_attractive_field = mag_attractive_field
        self.mag_tangencial_field = mag_tangencial_field
        self.goal = goal

    def calculate_force(self, position):
        angle = cart2polar(self.direction)[1]
        difference = position - self.origin
        force = np.array([0, 0])
        weight = 1.0
        if((np.fabs(angle - cart2polar(difference)[1]) <= weight*self.width) and (cart2polar(difference)[0] <= 0.4)):
            attractive_field = AttractivePotentialField(self.goal, self.mag_attractive_field)
            force = attractive_field.calculate_force(position)
            print 'ME SEGURA TO INDO'

        else:
            tangencial_field = TangencialPotentialField(self.origin, self.mag_tangencial_field)
            force = tangencial_field.calculate_force(position)
            print 'RODA A ROLETA'

        return force

class ConstantPotentialField:
    def __init__(self, field_force):
        self.field_force = field_force

    def calculate_force(self):
        return self.field_force

