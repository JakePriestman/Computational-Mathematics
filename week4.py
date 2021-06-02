# import files here

# 4A 
# function
from math import floor
from math import sqrt
from math import pi
from math import exp
from fractions import Fraction

def contfrac(n,terms):
    cf=[]
    while terms>0:
        cf.append(floor(n))
        n= 1/(n-floor(n))
        terms -=1
    return cf
# Answers to questions
print('Exercise 4A')
print('(i) What is the continued fraction expansion (to 20 terms) of sqrt(2)?')
print('The continued fraction expansion to 20 terms of sqrt(2) is,',contfrac(sqrt(2),20))
print('(ii) What is the continued fraction expansion (to 20 terms) of sqrt(3)?')
print('The continued fraction expansion to 20 terms of sqrt(3) is,',contfrac(sqrt(3),20))
print('(iii) What is the continued fraction expansion (to 20 terms) of sqrt(7)?')
print('The continued fraction expansion to 20 terms of sqrt(7) is,',contfrac(sqrt(7),20))
print('(iv) What is the continued fraction expansion (to 20 terms) of pi?')
print('The continued fraction expansion to 20 terms of pi is,',contfrac(pi,20))
print('(v) What is the continued fraction expansion (to 20 terms) of e?')
print('The continued fraction expansion to 20 terms of e is,',contfrac(exp(1),20))
print('(vi) If x = x_0 < 1, a_0 = floor(x_0) = 0. So, x_1 = 1/(x_0-a_0) = 1/x_0 > 1. Now, x_n >= a_n for any natural number n as if for some integer k, k < x_n < k+1, then a_n = k similarly if k+1 < x_n < k+2, a_n = k+1. However, if x_n = k, then a_n = k, in which case x is a rational number and has a finite continued fraction expression and the algorithm stops before this term. It follows that x_(n+1) = 1/(x_n-a_n) > 1. Hence a_(n+1) >= 1 for any natural number n greater than 0.')
print('If we increase the number of terms to 30 and repeat the alogrithm with sqrt(2) we find the continued fraction expression', contfrac(sqrt(2),30),'This is not exactly correct as sqrt(2) is irrational so the continued fraction expression is infinite.')
# 4B
# function
def contfrac2(num,den):
    cf=[]
    while den>0:
        cf.append(num//den)
        num = num % den
        num, den = den,num
    return cf

# Answers to questions
print('Exercise 4B')
print('(i) What is the continued fraction expasnsion of 97/61?')
print('The continued fraction expansion of 97/61 is,',contfrac2(97,61))
print('(ii) What is the continued fraction expasnsion of 1066/1012?')
print('The continued fraction expansion of 1066/1012 is,',contfrac2(1066,1012))
print('(iii) What is the continued fraction expasnsion of 123456789/987654321?')
print('The continued fraction expansion of 123456789/987654321 is,',contfrac2(123456789,987654321),'This is not the exact answer as it is 0.12 out from the true value.')

#4C
# function
def partcon(a,k):
    cf = contfrac(a,20)
    den = cf[k-1]
    num = 1
    for j in range(2,k+1):
        num = cf[k-j]*den+num
        num, den = den, num
    return Fraction(den,num)
#Answers to questions
print('Exercise 4C')
print('(i) Give the first five partial convergents to sqrt(2).')
print('The first five convergents to sqrt(2) are',partcon(sqrt(2),1),partcon(sqrt(2),2),partcon(sqrt(2),3),partcon(sqrt(2),4),partcon(sqrt(2),5))
print('(ii) What is the closest approximation to pi of all fractions with denominator at most 113?')
print('The closest approximation to pi of all fractions with denominator at most 113 is',partcon(pi,4))
print('(iii) What is the first partial convergent of sqrt(5) to be within 0.001% if the true value?')
print('The first partial convergent of sqrt(5) to be within 0.001% of the true value is',partcon(sqrt(5),5))
