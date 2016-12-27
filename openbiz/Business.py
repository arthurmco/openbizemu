""" Business base class and its relationed

    This file is part of OpenBIZ
"""

import random

class Building:
    
    def __init__(self, x, y, width, height):
        self.xPos = x
        self.yPos = y
        self.width = width
        self.height = height
        self.influence = max(width, height)
        self.employees = 1


class Business:
    maxID = 0

    def __init__(self, name, money = 0):
        Business.maxID += 1
        self.name = name
        self.bid = Business.maxID 
        self.category = 0
        self.money = money
        self.score = 0
        self.buildings = []


    @property
    def totalEmployees(self):
        """ The total employees count of the business """
        n = 0
        for b in self.buildings:
            n = n + b.employees

        return n
    
    def iterate(self):
        """ Iterate the business
            Check each building and tries to improve the influence area on it 
        """
        for b in self.buildings:
            b.influence = max(b.width, b.height) + \
                ((self.score+self.totalEmployees) / 1000)
            rnum = random.random()*self.totalEmployees*(b.influence*random.random())
            if rnum*random.random() > random.random()*80:
                b.employees += 1
                break


