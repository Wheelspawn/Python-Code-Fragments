#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 17:42:31 2018

@author: nsage
"""

def lSystem(s, variables, consts, rules, stop):
    '''
    S is the production string
    Variables are the vars the algorithm will be working with.
    Consts are like variables, but they are immutable once placed.
    Rules are a dictionary (of strings to strings) that specifies how to modify each var.
    The stop is an int that ends the recursion and returns the completed string.
    '''
    if stop != 0:
        new_s = ""
        for c in s:
            if c not in consts:
                new_s = new_s + rules[c]
            else:
                new_s = new_s + c
                
        return lSystem(new_s,variables,consts,rules,stop-1)
    else:
        return s

def lindenmayer_fib():
    '''
    Demo that shows how the fibonacci sequence can be generated
    if the rule is to replace A with AB and B with A.
    '''
    print("Strings:")
    s="A"
    v = ['A','B']
    c = ['C']
    r = {'A':'AB','B':'A'}
    
    for i in range(8):
        print(lSystem(s,v,c,r,i))
    
    print("")
    print("")
    print("Lengths:")
    
    for i in range(8):
        print(len(lSystem(s,v,c,r,i)))
        
def tree():
    '''
    A fractal tree.
    '''
    
    print("Strings:")
    s="0"
    v = ['0','1']
    c = [',']
    r = {'1':'11','0':'100'}
    
    for i in range(5):
        print(lSystem(s,v,c,r,i))