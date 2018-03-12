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
    
    a[0][0] = 2
    a[0][-1] = 3
    a[-1][0] = 4
    a[-1][-1] = 5
    
    disp(a,8,0,0,len(a)-1,len(a)-1)
    return a
    
def disp(a,r,top_x, top_y, bottom_x, bottom_y):
    
    if ( abs(top_x-bottom_x) >= 2 ) or ( abs(top_y-bottom_y) >= 2 ):
        
        mid_y = (top_y+bottom_y)//2
        mid_x = (top_x+bottom_x)//2
        
        # diamond step
        a[mid_x][mid_y] = int((a[0][0]+a[0][-1]+a[-1][0]+a[-1][-1])/4 + rand.randrange(-1,2)*r)
        
        # square step
        #  top, left, right, bottom, respectively        
        a[top_x][mid_y] = int((a[top_x][top_y] + a[top_x][bottom_y] + a[mid_x][mid_y])/3 + rand.randrange(-1,2)*r)
        a[mid_y][top_x] = int((a[top_x][top_y] + a[bottom_x][top_y] + a[mid_x][mid_y])/3 + rand.randrange(-1,2)*r)
        a[mid_y][bottom_x] = int((a[bottom_x][top_y] + a[bottom_x][bottom_y] + a[mid_x][mid_y])/3 + rand.randrange(-1,2)*r)
        a[bottom_x][mid_y] = int((a[top_x][bottom_y] + a[bottom_x][bottom_y] + a[mid_x][mid_y])/3 + rand.randrange(-1,2)*r)
        
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

def display(n):
                # ocean, desert, grass, forest, mountain
    terrain = [ '≈', '░', '`', '`', '¥', '^']
    for i in range(len(n)):
        for j in range(len(n[0])):
            if n[i][j] < 0:
                print(terrain[0], " ", end='')
            elif n[i][j] > 5:
                print(terrain[5], " ", end='')
            else:
                print(terrain[n[i][j]], " ", end='')
        print("")
        
def demo():    
    print('≈ :  ocean')
    print('░ :  desert')
    print('` :  grassland')
    print('¥ :  forest')
    print('^ :  mountain')
    print("creating map of size 25x25")
    m=create_map(25)
    display(m)
    
    print("")
    print("key:")
    print('` :  grassland')
    print('▒ :  ocean')
    print('░ :  desert')
    print('¥ :  forest')
    print('^ :  mountain')

demo()