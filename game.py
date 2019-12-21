#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 13:27:56 2019

@author: willdarden
"""

from Deck import Deck


rules = {
        "handSize": 5
        }


d = Deck()

print(d.drawCards(5))

print(d.deckCount())