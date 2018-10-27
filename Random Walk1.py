# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 17:42:45 2018

@author: Owner
"""

import random

"""Return coordinates after 'n' steps in random walk"""
def random_walk(n):
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N','S','E','W'])
        if step == 'N':
            y = y+1
        elif step == 'S':
            y = y-1
        elif step == 'E':
            x = x+1
        else:
            x = x-1
    return (x,y)

"""Compute distance from origin"""
for i in range(25):
    walk = random_walk(10)
    print(walk, "Distance from origin is: ",
          abs(walk[0])+abs(walk[1]))

"""Monte Carlo Simulation"""
"""If more than 4 blocks from origin, call an Uber, assuming you typically walk 1-30 blocks from home"""
number_of_walks = 10000

for walk_length in range(1,31):
    call_uber = 0 #Number of walks 4 blocks or fewer from home
    for i in range(number_of_walks):
        (x,y) = random_walk(walk_length)
        distance = abs(x) + abs(y)
        if distance >=4:
            call_uber += 1
    call_uber_percentage = float(call_uber)/number_of_walks
    print("Walk size = ",walk_length,
          "   % chance of calling Uber = ", 100*call_uber_percentage)

            
    