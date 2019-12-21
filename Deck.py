#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 13:08:36 2019

@author: willdarden
"""

from Enumerations import SUITES
from Card import Card
import random

class Deck:
    deck = []

    def __init__(self, shuffle = True, nDecks = 1):
        for d in range(nDecks):
            for s in SUITES:
                for i in range(13):
                    self.deck.append(Card(s, i))
        if shuffle:
            self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.deck)

    def drawCards(self, n = 1):
        res = []
        for i in range(n):
            res.append(self.deck.pop(0))
        return res
    
    def deckCount(self):
        return len(self.deck)
    
    def dump(self):
        for c in self.deck:
            c.dump()