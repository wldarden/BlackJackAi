#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 13:27:56 2019

@author: willdarden
"""

useModel = True
overWriteTrainingData = True # false for appending this run to results
logFile = './BlackJackAIDataLog.txt'

logFileMode = "a"
if overWriteTrainingData:
    logFileMode = "w"
from Deck import Deck
from Player import Player
from bjUtils import handValue

wins = 0.0
total = 0.0
try:
    modelWinPect
except NameError:
    modelWinPect = []
try:
    dealerStratPect
except NameError:
    dealerStratPect = []

class BlackJack:
    deck = []
    dealer = None
    players = []
    gameRound = 0
    gameID = 0
    logs = []
    wins = 0.0
    total = 0.0
    useModel = False
    def __init__(self, nDecks = 1, nPlayers = 1, useModel = False):
        self.useModel = useModel
        self.log = []
        self.deck = Deck(True, nDecks)
        self.dealer = Player('Dealer', 21, 'dealer')
        for p in range(nPlayers):
            pl = Player("player" + str(p), 1000, 'ai')
            self.players.append(pl)
    def hit(self):
        return self.deck.drawCards(1)[0]
    
    def deal(self):
        self.dealer.setHand(self.deck.drawCards(2))
        for p in self.players:
            p.setStanding(False)
            p.setHand(self.deck.drawCards(2))

    def dumpGameState(self):
        print("****************************")
        print("****Dumping Game State******")
        print("****************************")
        self.dealer.dump()
        for p in self.players:
            p.dump()
        print("****************************")
        print("****************************")
    
    def entityMove(self, entity, infoLog = True):
        if not entity.standing:
            move = entity.play(self.dealer, self.useModel)
            if infoLog:
                print(">>>>>>>%s elected to %s" % (entity.name, move))
            if move == 'hit':
                entity.hand.append(self.hit())

    def evaluateHand(self, p):
        pHasAce = False
        for c in p.hand:
            if c.value == 12:
                pHasAce = True
        res = {
                "pName": p.name,
                "dFaceValue": handValue([self.dealer.hand[0]]),
                "dHasAce": handValue([self.dealer.hand[0]]) == 11,
                "pScore": handValue(p.hand),
                "pHasAce": pHasAce,
                "DidHit": p.play(self.dealer, self.useModel) == 'hit'
                }
        return res
    
    def evaluateGame(self, gameLog):
        global total
        global wins
        dScore = handValue(self.dealer.hand)
        dBust = False
        if dScore > 21:
            dBust = True    
        
        pScores = []
        pHasAces = []
        log = []
        for p in self.players:
            pScore = handValue(p.hand)
            result = 'WIN'
            if pScore > 21:
                result = 'BUST'
            elif not dBust and pScore < dScore:
                result = 'LOST'
            elif not dBust and pScore == dScore:
                reulst = 'PUSH'
            pScores.append(pScore)
            pHasAce = False
            for l in gameLog:
                if l["pName"] == p.name:
                    l["win"] = result == 'WIN'
                    l["result"] = result
            for c in p.hand:
                if c.value == 12:
                    pHasAce = True
            pHasAces.append(pHasAce)
            total += 1
            if (l["win"]):
                wins += 1
        for i in range(len(gameLog)):
            l = gameLog[i]
            l["dBusted"] = dBust
            if l["win"]:
                l["class"] = 'should-hit' if l["DidHit"] else 'should-not-hit'
            else:
                if i == len(gameLog) - 1:  
                    if dBust and len(self.dealer.hand) == 3 and l['result'] == 'BUST':
                        l["class"] = 'should-not-hit'
                    elif l["result"] == 'BUST' and not dBust and handValue(p.hand[:len(p.hand)-1]) > dScore:
                        l["class"] = 'should-not-hit'
                    else:
                        l["class"] = 'should-not-hit' if l["DidHit"] else 'should-hit'
                else:
                    if l["result"] == 'BUST':
                        l['class'] = 'should-not-hit'
                    elif handValue(p.hand[:i]) > dScore:
                        l['class'] = 'should-not-hit'
                    elif pScore < dScore and pScore < 16:
                        l['class'] = 'should-hit'
                    else:
                        l["class"] = 'should-hit' if l["DidHit"] else 'should-not-hit'
                        
            log.append(l)
        return log

    def gameResult(self):
        dScore = handValue(self.dealer.hand)
        dBust = False
        if dScore > 21:
            print("Dealer has %d, Busted!" % dScore)
            dBust = True
        else:
            print("Dealer has %d" % dScore)
        for p in self.players:
            pScore = handValue(p.hand)
            result = 'WIN'
            if pScore > 21:
                result = 'BUST'
            elif not dBust and pScore < dScore:
                result = 'LOST'
            elif not dBust and pScore == dScore:
                reulst = 'PUSH'
            print("%s has %d. %s" % (p.name, pScore, result))

    def runGame(self, infoPrint = True, logGame = False):
        self.deal()
        if infoPrint:
            print("*****start*****")
            self.dumpGameState()
        gameLog = []
        while(any(not p.standing for p in self.players)):
            if infoPrint:
                print("\n***** Round %d *****" % self.gameRound)
            for p in range(len(self.players)):
                if not self.players[p].standing:
                    gameLog.append(self.evaluateHand(self.players[p]))
                            
            for p in self.players:
                self.entityMove(p, infoPrint)
            
            
            self.gameRound +=1
        if infoPrint:
            print("*****All players standing*****")
        while(not self.dealer.standing):
            self.entityMove(self.dealer, infoPrint)
        if infoPrint:
            print("*****Dealer standing*****")
            self.gameResult()
        if logGame:
            self.log = self.log + self.evaluateGame(gameLog)
        self.gameID += 1
        return self.log




print('using model: %i' % useModel)
bj = BlackJack(50,1, useModel)
log = []
for i in range(250):
    log = log + bj.runGame(False, logFile)
  

if useModel:
    modelWinPect.append(wins/total)
    f = open(logFile, logFileMode)
    results = []
    for l in log:
        s = ''
        for key in outCols:
            val = l[key]
            if type(val) == bool:
                val = 1 if val else 0
            s = s + str(val) + ','
        s = s[:-1]
        s = s + '\n'
        f.write(s)
        results.append(l["result"])
    f.close()
else:
    dealerStratPect.append(wins/total)
outCols = ["dFaceValue","dHasAce","pScore","pHasAce","class"]
print('wins: %d, total: %d, win pect: %f' % (wins, total, wins/total))




