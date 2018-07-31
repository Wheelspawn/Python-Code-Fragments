#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 19:56:11 2018

@author: nsage
"""

import numpy as np
import random as rand

class union_find(object):
    
    def __init__(self, sets=[]): # [row, col]
        self.sets = sets[:]
        
    def make_set(self, e):
        if e not in self.sets:
            self.sets.append(e)
    
    def union(self, a, b):
        found_a = self.find(a)
        found_b = self.find(b)
        
        c = (found_a+found_b)[:]
        
        print("Found a: ",found_a)
        print("Found b: ",found_b)
        
        self.sets.remove(found_a)
        if found_a != found_b:
            self.sets.remove(found_b)
        
        self.sets.append(c)
    
    def find(self, e):
        for i in range(len(self.sets)):
            if e in self.sets[i]:
                return self.sets[i]
        return False
    
class union_find_edge(union_find):
    def make_set(self, e):
        reverse_e = (e[1],e[0])
        if e not in self.sets and reverse_e not in self.sets:
            self.sets.append(e)
            


'''
u = union_find()
u.make_set(1)
u.make_set(2)
u.make_set(3)
u.make_set(4)
u.union(1,2)
u.union(3,4)
print(u.find(3))
print(u.find(5))
'''

def gen_maze(n): # only works for perfect squares! Do not use anything else!
    
    # a = np.ones((n,n))
    a = np.arange(0,n).reshape(int(np.sqrt(n)),int(np.sqrt(n)))
    
    e = union_find_edge()        # full edge list
    r = union_find_edge()        # removed edge list
    d = union_find()             # nums
    
    for i in range(n):
        d.make_set([i])
    
    for i in range(len(a)):
        for j in range(len(a[i])):
            if (i-1 >= 0):
                e.make_set( (a[i][j], a[i-1][j]) )
            if (i+1 < np.sqrt(n)):
                e.make_set( (a[i][j], a[i+1][j]) )
            if (j-1 >= 0):
                e.make_set( (a[i][j], a[i][j-1]) )
            if (j+1 < np.sqrt(n)):
                e.make_set( (a[i][j], a[i][j+1]) )
                
    edge_list = e.sets
    
    # print(edge_list)
    
    while (len(r.sets) < n-1):
        new_edge = rand.choice(edge_list)
        x=new_edge[0]
        y=new_edge[1]
        if x != y:
            d.union(x,y)
            r.make_set(new_edge)
            edge_list.remove(new_edge)
        else:
            print('f')



    return r    
