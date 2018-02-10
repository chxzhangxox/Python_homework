# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 10:35:37 2018

@author: chenxizhang
"""
import time



def f(x):
    return x**2

g = lambda x: x**2

N = 1000000
x = range(N)
y = []

#######for loop with f(x)#########

begin = time.clock()
for i in x:
    y.append(f(i))
end = time.clock()

print 'With f: ',end - begin

#######for loop with lambda function g###########
y = []

begin = time.clock()
for i in x:
    y.append(g(i))
end = time.clock()

print 'With lambda func g: ',end - begin

#######for loop without calling a function###########
y = []

begin = time.clock()
for i in x:
    y.append(i**2)
end = time.clock()

print 'append i**2 to empty list: ',end - begin

#######initialize y to range(N) first, then square elements#####
y = range(N)

begin = time.clock()
for i in y:
    y[i] = f(i)
    #y[i] = i**2
end = time.clock()

print 'modify existing list with f: ', end - begin
    
#######use list comprehension to generate#########
y = []
begin = time.clock()
y = [f(i) for i in range(N)]
#y = [i**2 for i in range(N)]
end = time.clock()

print 'list comprehension with f: ', end - begin

#######use map to generate the list of squares####
y = []
begin = time.clock()
y = map(f,range(N))
#y = [lambda i: i**2,range(N)]
end = time.clock()

print 'map with f: ',end - begin
















