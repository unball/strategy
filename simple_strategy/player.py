#!/usr/bin/env python
from abc import ABCMeta, abstractmethod

class Player(object):
    __metaclass__ = ABCMeta
    
    #returns a global point in the field
    @abstractmethod
    def getTarget(self):
        pass

    def setPositions(self, allies = [], enemies = [], ball = [], my_index = 0, field_side = 'left'):
        self.allies = allies
        self.enemies = enemies
        self.ball = ball
        self.my_index = my_index
        self.field_side = field_side