#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 19:56:11 2018

@author: nsage
"""

import numpy as np
import random as rand

def mid_disp(n):
    
    a=[ [0 for i in range(n)] for i in range(n)]
    
    a[0][0] = 20
    a[0][-1] = 30
    a[-1][0] = 40
    a[-1][-1] = 50
    
    disp(a,128,0,0,len(a)-1,len(a)-1)
    return a
    
def disp(a,r,top_x, top_y, bottom_x, bottom_y):
    
    if ( abs(top_x-bottom_x) >= 2 ) or ( abs(top_y-bottom_y) >= 2 ):
        
        mid_y = (top_y+bottom_y)//2
        mid_x = (top_x+bottom_x)//2
        
        # diamond step
        a[mid_x][mid_y] = int((a[0][0]+a[0][-1]+a[-1][0]+a[-1][-1])/4 + rand.randrange(-1,4)*r)
        
        # square step
        #  top, left, right, bottom, respectively        
        a[top_x][mid_y] = int((a[top_x][top_y] + a[top_x][bottom_y] + a[mid_x][mid_y])/3 + rand.randrange(-2,2)*r)
        a[mid_y][top_x] = int((a[top_x][top_y] + a[bottom_x][top_y] + a[mid_x][mid_y])/3 + rand.randrange(-1,4)*r)
        a[mid_y][bottom_x] = int((a[bottom_x][top_y] + a[bottom_x][bottom_y] + a[mid_x][mid_y])/3 + rand.randrange(-1,3)*r)
        a[bottom_x][mid_y] = int((a[top_x][bottom_y] + a[bottom_x][bottom_y] + a[mid_x][mid_y])/3 + rand.randrange(-3,2)*r)
        
        r *= (1/2)
        
        disp(a, r, top_x, top_y, mid_x, mid_y) # upper left
        disp(a, r, top_x, mid_y, mid_x, bottom_y) # upper right
        disp(a, r, mid_x, top_y, bottom_x, mid_y) # lower left
        disp(a, r, mid_x, mid_y, bottom_x, bottom_y) # bottom right
        
    else:
        return a

def create_map(n):
    m = mid_disp(n)
    return m

class World(object):
    
    def __init__(self, p_loc=0, p_pos=[5,5]): # [row, col]
        self.init()
    
    def init(self):
        
        self.first = Block(
            [ [2,2,4,2,4,4,2,4,4,2,2],
              [2,2,2,2,2,2,4,2,2,2,2],
              [0,2,2,2,2,2,2,2,2,2,5],
              [0,2,4,2,2,2,2,2,4,2,5],
              [2,2,2,2,2,2,2,2,2,2,5],
              [0,0,2,2,2,2,2,2,2,2,2],
              [0,0,0,2,2,2,2,2,2,4,5],
              [0,0,2,2,2,2,2,2,2,5,5],
              [0,2,2,2,2,2,2,2,2,2,5],
              [2,2,2,1,1,2,2,1,2,2,2],
              [2,2,1,1,1,1,1,1,1,2,2], ])
    
    def draw(self):
        n=self.first
                    # ocean, desert, grass, forest, mountain
        terrain = [ '≈', '░', ',', ',', '¥', '^']
        for i in range(len(n)):
            for j in range(len(n[0])):
                if (i==self.p_pos[0]) and (j==self.p_pos[1]):
                    print("@", " ", end='')
                elif n[i][j] < 0:
                    print(terrain[0], " ", end='')
                elif n[i][j] > 5:
                    print(terrain[5], " ", end='')
                else:
                    print(terrain[n[i][j]], " ", end='')
            print("")

class Block(object):
    def __init__(self, t=[], neighbors=[[],[],[]]): # [row, col]
        self.t = t
        self.neighbors=neighbors
        self.init()
    
    def init(self):
        for i in range(0,3):
            for j in range(0,3):
                self.neighbors[i][j] = np.ones([11,11],dtype='int')*-1
        
def blank_block():
    return np.ones([11,11],dtype='int')*-1

def display(n,x,y):
            # ocean, desert, grass, forest, mountain
    terrain = [ '≈', '░', ',', ',', '¥', '^']
    for i in range(len(n)):
        for j in range(len(n[0])):
            try:
                if (i==5) and (j==5):
                    print("@", " ", end='')
                elif n[i][j] < 0:
                    print(terrain[0], " ", end='')
                elif n[i][j] > 5:
                    print(terrain[5], " ", end='')
                else:
                    print(terrain[n[i][j]], " ", end='')
                    
            except IndexError:
                print('', "~", end='')
                
        print("")
        
m=create_map(5**4)

# import readchar
# print(type(a))
# print(a)

def loopy_loop(): 
    player_x = 40
    player_y = 40
    
    a=[ [m[i][j] for i in range(player_x-5,player_x+6)] for j in range(player_y-5,player_y+6)]
    display(a,player_x,player_y)
    
    s=input()
        
    while (s != 'q' or s != 'Q'):
        
        a=[ [m[i][j] for i in range(player_x-5,player_x+6)] for j in range(player_y-5,player_y+6)]
        display(a,player_x,player_y)
        
        s=input()
        
        if s == 'w':
            player_y -= 1
        elif s == 'a':
            player_x -= 1
        elif s == 's':
            player_y += 1
        elif s == 'd':
            player_x += 1
        elif s == 'q':
            break
        
def demo():    
    print('≈ :  ocean')
    print('░ :  desert')
    print('` :  grassland')
    print('¥ :  forest')
    print('^ :  mountain')
    print("creating map of size 25x25")
    m=create_map(25)
    display(m,12,12)
    
    print("")
    print("key:")
    print('` :  grassland')
    print('▒ :  ocean')
    print('░ :  desert')
    print('¥ :  forest')
    print('^ :  mountain')