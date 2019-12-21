#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:23:55 2019

@author: willdarden
"""

from BlackJackAI import BlackJackAI as ai
from bjUtils import handValue

class Player:
    pType = 'human'
    name = 'player'
    ai = None
    cash = 0
    hand = []
    standing = False

    def setStanding(self, s = False):
        self.standing = s
    def __init__(self, name, cash, pType):
        self.name = name
        self.cash = cash
        self.pType = pType
        if pType == 'ai':
            self.ai = ai()
        elif pType == 'dealer':
            self.ai = ai('dealer')

    def setHand(self, hand):
        self.hand = hand

    def play(self, dealer, useModel = False):
        move = ''
        if self.pType == 'human':
            move = input("player input here: ")
            self.standing = move == 'stand'
        else:
            move = ai.play(ai.aiType, self, dealer, useModel)
            if move == 'stand':
                self.standing = True
            return move
                

    def dumpHand(self):
        for c in self.hand:
            c.dump()
        print("Hand Value: %d" % handValue(self.hand))
        
    def dumpPlayer(self):
        print("player: %s, cash: %d" % (self.name, self.cash))
    
    def dump(self):
        self.dumpPlayer()
        self.dumpHand()
        
        
        
        










