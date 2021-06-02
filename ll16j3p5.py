from math import sin
from math import cos
from math import pi
from math import sqrt
from math import atan
from math import factorial

#Exercise 5A
#(1)
def cube(x):
    return x**3

#(2)
def sum_diff(x,y):
    return(x+y,x-y)

#(3)
def trigid(x):
    return 1

#(4)
def fib(n):
    fiblist = [1]
    fn = 1
    fm = 1
    while len(fiblist) < n:
        if n >= 3:
            fiblist.append(fn+fm)
            fn, fm = fn+fm, fn
        elif n == 2:
            fiblist.append(fm)
    return fiblist

#(5)
def polar(r,theta):
    return (r*cos(theta),r*sin(theta))

#(6)
def cart(x,y):
    r = sqrt(x**2+y**2)
    if x == 0 and y > 0:
        theta = pi/2
    elif x == 0 and y < 0:
        theta = -pi/2
    elif x < 0 and y > 0:
        theta = atan(pi-y/x)
    elif x < 0 and y < 0:
        theta = atan(y/x-pi)
    elif x > 0 and y > 0:
        theta = atan(y/x)
    elif x > 0 and y < 0:
        theta = atan(-y/x)
    return (r,theta)

#Exercise 5B
#(1)
def poly(x0,coeffs):
    a = 0
    for i in range(len(coeffs)):
        a += coeffs[i]*x0**i
    return a

#(2a)
    
print(poly(6,[2,3,0,1]))

#(2b)
print(poly(sqrt(2),[2,0,-1]))
print('The answer to 2a is exact but for 2b python converts sqrt(2) into a float which does not represent the exact value fro sqrt(2).')

#(3)
def horner(x,coeffs):
    coeffs.reverse()
    b = 0
    for a in coeffs:
        b = a+x*b
    return b


def poly2(x0,coeffs):
    a = 0
    for i in range(len(coeffs)):
        a += i*coeffs[i]*x0**(i-1)
    return a

#(4a)
print(poly(1,[0,0,1,-4,0,7]))
print(poly2(1,[0,0,1,-4,0,7]))

#(4b)
print(poly(pi,[0,0,1,-4,0,7]))
print(poly2(pi,[0,0,1,-4,0,7]))

#(5)
print(horner(pi/4,[0,1,0,-1/factorial(3),0,1/factorial(5),0,-1/factorial(7)]))