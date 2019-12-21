#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:17:27 2019

@author: willdarden
"""
from bjUtils import handValue
import pickle
import random
model = None
with open('aiFile.mod', 'rb') as file:
    model = pickle.load(file)

class BlackJackAI:
    aiType = ''
    def __init__(self, aiType = 'aiplayer'):
        self.aiType = aiType

    def play(aType, player, dealer, useModel = False):
        value = handValue(player.hand)
        if aType == 'dealer':
            if value <= 16:
                return 'hit'
            else:
                return 'stand'
        else:
            if value > 21:
                return 'stand'
            if useModel:
                hasAce = False
                for c in player.hand:
                    if c.value == 12:
                        hasAce = True
                modelInput = [[handValue([dealer.hand[0]]), dealer.hand[0].value == 12, value, hasAce]]
#                print(model.predict(modelInput))
                return 'hit' if model.predict(modelInput)[0] == 1 else 'stand'
            else:
#                return 'hit' if random.uniform(0, 1) > .5 else 'stand'
                if value <= 16:
                    return 'hit'
                else:
                    return 'stand'