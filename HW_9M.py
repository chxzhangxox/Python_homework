# -*- coding: utf-8 -*-
"""
Created on Tue Mar 06 23:14:42 2018

@author: chxzh
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate as spint

#a*(sin(theta)) + b*theta prime + c*theta double prime = 0
def pend(y,t,*args):
    y1, y2 = y
    b, c = args
    dydt = [y2, (-a*np.sin(y1) - b*y2)/c ]
    return dydt
    
    
m = 1.0
l = 1.0
g = 1.0

p1 = m
p2 = g
p3 = l

a = -p1*p2*p3
b = 0.0
c = -p1*p3**2

y0 = [1,0]
t = np.linspace(0,10,101)

sol = spint.odeint(pend, y0, t, args = (b,c))
plt.plot(t,sol[:,0])