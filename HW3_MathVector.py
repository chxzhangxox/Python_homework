# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 10:42:02 2018

@author: chxzh
"""

class MathVector:
    """MathVector class, storing vectors"""
    def __init__(self,*args):
        if len(args) == 1 and isinstance(args[0],(int,long)):
            self.vec = [0] * args[0]
        elif len(args) == 1 and isinstance(args[0],list):
            self.vec = args[0]
        elif len(args) == 1 and isinstance(args[0],tuple):
            self.vec = list(args[0])
        else:
            self.vec = [args[i] for i in range(len(args))]
    
    def get_el(self, i):
        return self.vec[i-1]
    
    def neg(self):
        neg = MathVector(self.vec)
        neg.vec = [-x for x in neg.vec]
        return neg
    
    def mag(self):
        mag = sum(self.vec[i]**2 for i in range(len(self.vec)))**(0.5)
        return mag
    
    def dot(self,other):
        dot = sum(self.vec[i] * other.vec[i] for i in range(len(self.vec)))
        return dot
    
    def plus(self,other):
        plus = [a+b for a,b in zip(self.vec,other.vec)]
        return MathVector(plus)
    
    def sp(self,scalar):
        scalar_vec = [scalar*i for i in self.vec]
        sp = MathVector(scalar_vec)
        return sp
    
    def print_me(self):
        print self.vec
        
    def __getitem__(self,i):
        return self.get_el(i)
    
    def __neg__(self):
        return self.neg()
    
    def __abs__(self):
        return self.mag()
    
    def __mul__(self,other):
        if isinstance(other,MathVector):
            return self.dot(other)
        else:
            return self.sp(other)
    
    __rmul__ = __mul__
    
    def __add__(self,other):
        return self.plus(other)
    
    def __str__(self):
        return str(self.vec)
    
    
    
    
    
    
    