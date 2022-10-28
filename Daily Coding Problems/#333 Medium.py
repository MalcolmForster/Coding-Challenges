# At a party, there is a single person who everyone knows, but who does not know anyone in return (the "celebrity"). To help figure out who this is, you have access to an O(1) method called knows(a, b), which returns True if person a knows person b, else False.
# Given a list of N people and the above operation, find a way to identify the celebrity in O(N) time.
from random import random

partySize = 100
celebNum = 87

def CreateParty():
    setParty = [Person(False) for i in range(partySize)]
    setParty[celebNum] = Person(True)
    return setParty

class Person():
    def __init__(self, celeb):
        self.celeb = celeb
        self.knowsList = [celebNum]
        if(celeb is False):
            for i in range(partySize):
                chance = 0.3 #per
                if(i != celebNum and random() < chance):
                    self.knowsList.append(i)        
    def isCeleb(self):
        return self.celeb
    def personKnows(self):
        return self.knowsList

def knows(a,b):
    aKnows = a.personKnows()
    if(b in aKnows):
        return True
    else:
        return False

N = CreateParty()

NotCeleb = []

currentPerson=0
for i in range(partySize-1):
    #print(p.personKnows())
    if(knows(N[currentPerson],i+1)):
        currentPerson = i+1

print('The celebrity is person ' + str(currentPerson))
        
        
    
