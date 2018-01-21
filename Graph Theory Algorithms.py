# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 14:46:57 2018

@author: Nathaniel
"""

def isGraphic(l): # checks to see if a degree list is graphic
    if l[0] > len(l)-1: # if a vertex has an extra edge
        return False
    else:
        if sum(l) == 0: # if vertex elimination is complete
            return True
        else: # delete the highest degree vertex
            v = l[0]
            l = l[1:]
            for i in range(v):
                l[i] -= 1
            l.sort(reverse=True)
            print(l)            
            return isGraphic(l) # recursive call