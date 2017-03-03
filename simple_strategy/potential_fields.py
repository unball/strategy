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
        difference = cart2polar(self.origin - position)
        difference *= np.array([self.magnitude, 1])

        if(difference[0] < self.min_magnitude):
            difference[0] = self.min_magnitude

        return polar2cart(difference)

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

