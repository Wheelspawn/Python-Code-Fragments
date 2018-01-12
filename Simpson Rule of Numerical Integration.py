# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 15:25:13 2018

@author: Nathaniel
"""

import numpy as np
import pylab

def area(a, b, function, steps=1024.0): # use Simpson's rule to estimate area under curve
    area = 0
    h = (b-a)/steps # calculate step size
    segs = np.arange(a,b,(b-a)/steps) # get the x-value of each step
    for i in range(len(segs)-1): # sum the area under the cubic polynomials
        area += (h/6)*(function(segs[i])
        + 4*function((segs[i+1]+segs[i])/2.0)
        + function(segs[i+1]))
    return area

def plot_area(a, b, function, steps=1024.0):
    
    x = np.arange(-5,5,0.01)
    y = []
    for i in range(len(x)):
        y.append(function(x[i]))
    approx_area = area(a, b, function, steps)
    pylab.plot(x,y,linewidth='2.5', label='6000 K')
    pylab.plot([-5,5],[0,0],linewidth='1.0',color='k') # x-axis
    pylab.plot([0,0],[-5,5],linewidth='1.0',color='k') # y-axis
    # sloice = x[x.index(a):x.index(b)]
    pylab.fill(x[550:650],y[550:650],color='0.8')
    pylab.fill([ x[550], x[550], x[650], x[650] ],[ 0, y[550], y[649], 0 ],
               color='0.8')
    pylab.text(0.75,0.75, 'A: ' + str(round(approx_area, 4)), fontsize=8)
    
    pylab.xlabel('X')
    pylab.ylabel('Y')
    pylab.xlim(-5,5)
    pylab.ylim(-5,5)
    pylab.grid()
    pylab.show()
    
def plot():
    plot_area(0.5,1.5,cubic,steps=1024.0)

def cubic(x):
    y = -x**3 + 4*x + 1
    return y

print("Area under cubic curve -x^3 + 4*x + 1 from 0.5 to 1.5")
print("128 steps: ", area(0.5,1.5,cubic,steps=128.0))
print("256 steps: ", area(0.5,1.5,cubic,steps=256.0))
print("512 steps: ", area(0.5,1.5,cubic,steps=512.0))
print("1024 steps: ", area(0.5,1.5,cubic,steps=1024.0))
print("Actual area: 3.75" )
print("Type plot() in the console to see a matplotlib graph.")