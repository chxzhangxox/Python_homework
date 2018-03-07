# -*- coding: utf-8 -*-
"""
Created on Sat Mar 03 12:59:20 2018

Find the largest area that can be enclosed by a curve with a given length

@author: Chenxi Zhang
"""
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

#generate points based on a guess
def z2xy(z):
    x = np.linspace(0,z[0], N)
    y = np.append(z[1:], [0])
    return x, y

#object function that we want to optimize
#compute the area and return the negative of the area
def obj(z):
    x_pts, y_pts = z2xy(z)
    area = sp.integrate.trapz(y_pts,x = x_pts)
    return sp.negative(area)

#define constraint function on the length
def con(z):
    x_pts, y_pts = z2xy(z)
    temp1 = y_pts[:y_pts.size-1]
    temp2 = y_pts[1:]
    x_sqr = (x_pts[1] - x_pts[0]) ** 2
    y_sqr = (np.subtract(temp2,temp1))**2
    l = np.sum(np.sqrt(x_sqr + y_sqr))
    return l - P
    
    

#number of decision variables, perimeter
N = 50
P = sp.pi/2

#50 sample points on a quarter unit circle
x = np.linspace(0,1,50)
y = np.abs(np.sqrt(1-x**2))

# a "perfect" guess of 50 decision variables
z0 = np.concatenate(([x[N-1]],y[:N-1]))

#generate a bound for decision variables
bound = [(0,P) for i in range(50)]
#generate a dictionary for constraints
dic_eq = {'type': 'eq', 'fun': con}

#call minimize function
min_para = sp.optimize.minimize(obj, z0, bounds = bound, constraints = dic_eq)
min_area = obj(min_para.x)
print min_area

#plot the graph with the perfect guess
plt.plot(x, min_para.x)

#random number between 0 and P
z1 = np.random.uniform(0,P,50)
min_para1 = sp.optimize.minimize(obj, z1, bounds = bound, constraints = dic_eq)
#plot the guess and the result
plt.plot(x, min_para1.x, label = 'solution')
plt.plot(np.linspace(0,P), z1, label = 'guess')
plt.legend()
plt.xlim((0,2))
plt.ylim((0,2))
plt.xticks(np.arange(0,2,0.5))
plt.yticks(np.arange(0,2,0.5))
plt.axis("equal")