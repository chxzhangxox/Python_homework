# -*- coding: utf-8 -*-
"""
A SIMPLE ALGORITHM
Calculate one root of a function using Newton's method
"""

import math



def f(x):
    return math.log(x) - 1

def diff_f(x):
    return 1/x

init_x = 1.5
error = 0.0001


while abs(f(init_x)) > error:
    delta = - f(init_x)/diff_f(init_x)
    init_x = init_x + delta

print 'One solution is: ' 
print init_x
    
   