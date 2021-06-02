# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("Exercise 1.A")
print("(i) On what day does Easter Sunday 2034 fall?")
from math import floor
a = 2034 % 19
b = 2034 % 4
c = 2034 % 7
k = floor(2034/100)
p = floor((13+8*k)/25)
q = floor(k/4)
M = (15-p+k-q) % 30
N = (4+k-q) % 7
d = (19*a+M) % 30
e = (2*b+4*c+6*d+N) % 7
print("Then Easter Sunday 2034 is",22+d+e,"March or",d+e-9,"April") 
print("As 40 March is not a real date, it is 9 April.")

print("(ii) What day of the week is Christmas Day this year?")
Q = 25
m = 12
K = 18
J = 20
h = (Q+floor((13*(m+1))/5)+K+floor(K/4)+floor(J/4)-2*J) % 7
print("As we get",h,", Christmas Day falls on a Tuesday.")

print("(iii) On what day of the week is Yorkshire Day 2019?")
Q = 1
m = 8
K = 19
J = 20
h = (Q+floor((13*(m+1))/5)+K+floor(K/4)+floor(J/4)-2*J) % 7
print("As we get",h,", Yorkshire Day falls on a Thursday.")

print("(iV) On what day of the week was Charles Babbage born?")
Q = 26
m = 12
K = 71
J = 19
h = (Q+floor((13*(m+1))/5)+K+floor(K/4)+floor(J/4)-2*J) % 7
print("As we get",h,", Charles Babbage was born on a Sunday")

print("Exercise 1.B")
print("(i) What commaned will produce a list of all odd integers from 1 to 100 inclusive?")
a = list(range(1,101,2))
print("Let a = list(range(1,101,2)). This command will create the list")
print(a)
print("(i) What commaned will produce a list of all even integers from 1 to 100 inclusive?")
a = list(range(2,101,2))
print("Let a = list(range(2,101,2)). This command will create the list")
print(a)
print("(iii) What is the 3rd element of the list a produced by a = list(range(70,1030,3))")
a = list(range(70,1030,3))
c = a[2]
print("The command a[2] gives the third entry of the list a. So the third entry is",c)
print("(iv) What is the penultimate element of the list b produced by b =list(range(-41,10))?")
b =list(range(-41,10))
d = b[-1]
print("The command b[-1] gives the penultamite entry of the list a. So the third entry is",d)
print("(v) What is the middle element of the list c produced by c = 10*a+5*b")
c = (10*a)+5*b
mid = c[len(c)//2]
print("To find the middle element of c we use the command c[len(c)//2]. So the middle element of c is",mid)
print("(vi) What are the equivalent expressions for the vector dot and cross products x.y and x x y?")
x = [1,3,5]
y = [2,4,6]
dot = x[0]*y[0]+x[1]*y[1]+x[2]*y[2]
cross  = ((x[1]*y[2]-x[2]*y[1]),(x[0]*y[2]-x[2]*y[0]),(x[0]*y[1]-x[1]*y[0]))
print("x.y = x[0]*y[0]+x[1]*y[1]+x[2]*y[2] =",dot,"and x x y = ((x[1]*y[2]-x[2]*y[1]),(x[0]*y[2]-x[2]*y[0]),(x[0]*y[1]-x[1]*y[0]))=",cross)