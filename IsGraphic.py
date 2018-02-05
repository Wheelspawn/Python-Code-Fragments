#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 12:49:53 2018

A program that will tell if a given degree sequence is graphic.
Uses the Havel-Hakimi algorithm. Returns a boolean.
Steps are printed to console.

@author: nsage
"""

def is_graphic(l): # checks to see if a degree list is graphic
     # if a vertex has an extra edge
     # or the sum is odd (sum of the degrees of v must be 2|e|)
    if l[0] > len(l)-1 or sum(l)%2==1:
        return False
    else:
        if sum(l) == 0: # if vertex elimination is complete
            return True
        else: # delete the highest degree vertex
            v = l[0]
            l = l[1:]
            for i in range(v): # decrement the next v indices
                l[i] -= 1
            
            for j in range(len(l)-1,0,-1): # remove the zeros at the end
                if l[j] == 0:
                    l.remove(l[j])
                else:
                    break
            
            l.sort(reverse=True)
            print(l)            
            return is_graphic(l) # recursive call

