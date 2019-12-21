#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:53:08 2019

@author: willdarden
"""

def handValue(hand):
        total = 0
        aces = 0
        for c in hand:
            if (c.value < 9):
                total += c.value + 2
            elif c.value == 12:
                aces += 1
            else:
                total += 10
        if (aces > 0):
            if (total + aces > 21):
                total = total + aces
            else:
                if (total + 11 + (aces - 1) < 21):
                    total = total + 11 + (aces - 1)
                else:
                    total = total + aces
        return total
