# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 12:45:12 2018

@author: jaki"""

import matplotlib.pyplot as plt
from random import randint
from statistics import mean, stdev

def initial_values(k):
    x = []
    for i in range(k):
        x.append(1)
    return x

def lagged_fib(j,k,M,n):
    m = 2**M
    x = initial_values(k)
    for i in range(n+1):
        FI = (x[i-j]+x[i-k]) % m
        x.append(FI)
    return x[k:-1]

print(lagged_fib(7,10,32,2000))

x = lagged_fib(7,10,32,2000)
x1 = [0]+lagged_fib(7,10,32,1999)

plt.figure('Figure A')
plt.xlabel('x_i')
plt.ylabel('x_(i-1)')
plt.plot(x,x1,'o')


z = [randint(0,2**32) for x in range(2000)]
z1 = [0] + [randint(0,2**32) for x in range(1999)]

plt.figure('Figure B')
plt.xlabel('z_i')
plt.ylabel('z_(i-1)')
plt.plot(z,z1,'o')
plt.plot(x=mean(x))




print('The mean of x_i is',mean(x),' and the mean of z_i is',mean(z),'. Comparing the means of both x_i and z_i, it can be seen that they are not comparable and are both completely different numbers.')
print('The standard deviation of x_i is',stdev(x),'and the standard deviation of z_i is',stdev(z),'. Comparing the standard deviations of x_i and z_i, they are completely differnet and not comparable.')
