#!/usr/bin/python

from openbiz.Business import *
import random
import time
from threading import Thread
""" Main OpenBIZ executable """

class GameTime:
    def __init__(self):
        self.day = 0
        self.isRunning = True
        self.stopGame = False

class ThreadRun(Thread):
    def __init__(self, business, gtime):
        Thread.__init__(self)
        self.business = business
        self.day = 0
        self.gtime = gtime

    def run(self):
        while not self.gtime.stopGame:
            self.business.iterate()
            self.gtime.day += 1
            time.sleep(0.2)


bname = raw_input("Type your business name: ")
xPos = random.randint(0, 10000)
yPos = random.randint(0, 10000)

building = Building(xPos, yPos, 10, 10)
business = Business(bname, random.randint(10000, 15000))
business.buildings.append(building)

gtime = GameTime()
tr = ThreadRun(business, gtime)
tr.start()

commands = ['day','employees']
print('You just started a new enterprise. You have {}$ of money'.format(business.money))
while not gtime.stopGame:
    try:
        print('\nDay {}, {} employees'.format(gtime.day, business.totalEmployees))
        command = raw_input('\033[1mmybiz>\033[0m ')
        command = command.strip()

        if command == '':
            continue

        if command == 'day':
            print(gtime.day)
        elif command == 'employees':
            print(business.totalEmployees)
        elif command == 'size':
            print('Default building size: {}x{} (at {},{})'.format(
                building.width, building.height, building.yPos, building.xPos))
        elif command == 'influence':
            print('Influence area: {}x{}'.format(
                building.influence, building.influence))
        else:
            print('Unknown command: %s'% command)

    except KeyboardInterrupt:
        gtime.stopGame = True

print('Exiting...')