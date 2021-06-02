# Template file for Week 2
# Lines that start with '#'
# are comments and are ignored
# by Python.

# Insert your Euclid algorithm program lines here:
print("This program will find the gcd of any two numbers.")
a=int(input('Please enter a value for a: '))
b=int(input('Please enter a value for b: '))
c=a
d=b
if a == 0:
    gcd = b
while b > 0:
    if a>b:
        t = b
        b = a % b
        a = t
    elif a<b:
        a,b = b,a
        t = b
        b = a % b
        a = t
gcd = a
print("So, the gcd(",c,",",d,") =",a)

    

# Give the answers to the questions below:
# gcd(105,24) = 3
# gcd(6024,1284)= 12
# gcd(98777,12945) = 1

# Insert your Extended Euclid algorithm program here:
print("This program executes the extended Euclidean algorithm. It will give you the numbers that satisfy the equation ax+by=gcd(a,b).")
a=int(input('Please enter a value for a: '))
b=int(input('Please enter a value for b: '))

x, xprev, y, yprev = 0,1,1,0
while b > 0:
    q = a//b
    a, b = b, a % b
    x, xprev = xprev - q*x, x
    y, yprev = yprev - q*y, y
print("So, gcd(a,b), x and y is",a,xprev,yprev,"respectively.")

# Insert your counting-steps Euclid program here:
from math import log
from math import pi
from math import e
print("This program will find the gcd of any two numbers and tell you how many steps it took to find it.")
a=int(input('Please enter a value for a: '))
b=int(input('Please enter a value for b: '))
count=0
c=a
d=b
if a == 0:
    gcd = b
while b > 0:
    if a>b:
        t = b
        b = a % b
        a = t
        count +=1
    elif a<b:
        a,b = b,a
        t = b
        b = a % b
        a = t
        count +=1
gcd = a
Max=5*log(c,10)
average=((12*log(2,e))/pi**2)*log(c)
print("So, the gcd(",c,",",d,") =",a)
print("The number of steps to find this was",count)
print('The maximum amount of steps to do this is',Max)
print('The average number of steps to do this is',average)

# Give examples of a,b which produce larger
# and smaller number of steps than the average
# here:
#a = 999, b = 69, number of steps is 3
#a = 98777, b = 81527, number of steps is 13
#
#
#
