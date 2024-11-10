import random
from random import randint

class RandomizedSet:

    def __init__(self):
        self.tab = []

    def insert(self, val: int) -> bool:
        if val in self.tab:
            return False
        else:
            self.tab.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.tab:
            return False
        else:
            self.tab.remove(val)
            return True

    def getRandom(self) -> int:
        l = len(self.tab)
        if l == 1:
            return self.tab[0]
        else:
            return self.tab[randint(0,l - 1)]