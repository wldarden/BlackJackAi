#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 13:11:07 2019

@author: willdarden
"""
from Enumerations import SUITES

class Card:
    suite = ''
    value = 0

    def __init__(self, s, v):
        if s in SUITES:
            self.suite = s
        else:
            raise Exception("Invalid Suite %s given to card." % s)
        if v >= 0 and v < 13:
            self.value = v
        else:
            raise Exception("Invalid value %d given to card." % v)
    
    def dump(self, useLabel = True):
        if useLabel:
            print("%s %s" % (str(self.label()), self.suite))
        else:
            print("%d %s" % (self.value, self.suite))
    
    def label(self):
        v = self.value
        if v < 9:
            return v + 2
        else:
            if v == 9:
                return 'Jack'
            if v == 10:
                return 'Queen'
            if v == 11:
                return 'King'
            if v == 12:
                return 'Ace'