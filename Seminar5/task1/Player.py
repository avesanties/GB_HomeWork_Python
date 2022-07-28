from Pot import *

class Player():
    MAX_TAKE : int
    pl_pot : Pot

    def __init__(self,name):
        self.name = name

    def take_sweets(self):
        __sweets += 1
        return 1

    def player_name(self):
        return self.name

class Human_Being(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def take_sweets(self):
        __amount = -1
        while not (0 < __amount <= super().MAX_TAKE):
            __amount = int(input())
            if not (0 < __amount <= super().MAX_TAKE):
                print('Wrong input provided!')
        return __amount

from random import randrange

class Bot(Player):

    def __init__(self, name):
        super().__init__(name)
    
    def take_sweets(self):
        __amount = self.pl_pot.sweets_left % (super().MAX_TAKE + 1)
        if __amount == 0:
            return randrange(1,super().MAX_TAKE + 1,1)
        return __amount