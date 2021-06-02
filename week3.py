# Template file for Week 3
# Lines that start with '#'
# are comments and are ignored
# by Python.

# Write your functions for 3A below
# E.g.,

#Returns x**3
def cubed(x):
    xxx = x**3
    return(xxx)
print('This will cube any number you input.')
cubenum = int(input('Give a number you would like to be cubed:'))
print(cubed(cubenum))


#Mean of two numbers
def mean(x,y):
    u = (x+y)*0.5
    return(u)
print('This will find the mean of two numbers.')
mean1 = int(input('Give one number:'))
mean2 = int(input('Give another number:'))
print('The mean of', mean1,'and', mean2, 'is', mean(mean1,mean2))


#Checks for pythagorian triangle
def pythagoras(a,b,c):
    list = [a,b,c]
    list.sort()
    if list[0]**2+list[1]**2==list[2]**2:
        return("True")
    else:
        return("False")
print('This will return True if the three numbers you give are a pythagorian triple or False if not.')
pythag1 = int(input('Give one number:'))
pythag2 = int(input('Give another number:'))
pythag3 = int(input('Give another number:'))
print(pythagoras(pythag1,pythag2,pythag3))


#Mean of a list
def mean_of_list(a):
    sum=0
    for i in a:
        sum = sum+i
    avg=(sum/len(a))
    return(avg)
print('This will give the mean of the list of numbers you give.')
meanlist = [int(x) for x in input('Give as many number you want with spaces between them:').split()]
print('The mean of',meanlist,'=',mean_of_list(meanlist))


#Finds greatest common divisor
def gcd(a,b):
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
    if a == b:
        gcd = a
    return(gcd)
print('This will find the Greatest Common Divisor of two numbers.')
gcd1 = int(input('Give one number:'))
gcd2 = int(input('Give a different number:'))
print('The gcd(',gcd1,',',gcd2,') = ', gcd(gcd1,gcd2))


#Takes decimal to binary
def dec_to_bin(x):
    decimal , binary =x,[]
    while decimal >0:
        binary.append(decimal % 2)
        decimal=decimal//2
    binary.reverse()
    return(binary)
print('This will convert a decimal integer to a binary expression.' )
dec = int(input('Give a number you want to convert into binary:'))
print('The binary representation of',dec, 'is', dec_to_bin(dec))


#Takes binary to decimal
#I have done this two ways and couldnt decide which one was better
def bin_to_dec(x):
    binary=x
    decimal = 0
    binary.reverse()
    for i in range(len(binary)):
        decimal = decimal + (2**i)*binary[i]
    return(decimal)
print('This will take a binary number and give you the decimal integer representation.')
bin1 = [int(x) for x in input('Type a binary expression with spaces inbetween the digits:').split()]
print('The decimal representation of',bin1,'is',bin_to_dec(bin1))


def bin_to_dec(x):
    binary=x
    decimal = 0
    for i in binary:
        decimal = decimal*2 + int(i)
    return(decimal)
print('This will take a binary number and give you the decimal integer representation.')
bin1 = list(input('Give a number of 1 and 0 digits:'))
print('The decimal representation of',bin1,'is',bin_to_dec(bin1))




#Takes date to day of the week
from math import floor
def day_of_the_week(date,month,year):
    Q = date
    M = month
    K = year % 100
    J = year//100
    h = (Q+floor((13*(M+1))/5)+K+floor(K/4)+floor(J/4)-2*J) % 7
    if h==0:
        return("Saturday")
    elif h==1:
        return("Sunday")
    elif h==2:
        return("Monday")
    elif h==3:
        return("Tuesday")
    elif h==4:
        return("Wednesday")
    elif h==5:
        return("Thursday")
    elif h==6:
        return("Friday")
print('This will tell you the day of the week of any date in the past or in the future.')
date = int(input('Give any date of a month:'))
month = int(input('Give any month represented by number:'))
year = int(input('Give any year:'))
print(date,'/',month,'/',year,'is a',day_of_the_week(date,month,year))


# Write your Eratosthenes function below

#Gives nth prime number.
def eratosthenes(max_prime):
    primes = [2]
    prime = 3
    while len(primes) < max_prime:
        for p in primes:
            if prime % p == 0:
                break
        else:
            primes.append(prime)
        prime+=2
    return(primes[-1])
print('This will give you the nth prime number of your choice.')
userprime = int(input('Give the nth prime number you want to know:'))
print('The',userprime,'th prime number is',eratosthenes(userprime))


# Give number of primes between two values.
def num_of_primes(max_prime):
    primes = list(range(2,max_prime+1))
    for i in primes:
        j=2
        while i*j <= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j += 1
    return len(primes)
print('This will give you the number of prime numbers between two numbers.')
usermaxprime1 =int(input('Give a number:'))
usermaxprime2 = int(input('Give a smaller number:'))
num_of_user_primes = num_of_primes(usermaxprime1) - num_of_primes(usermaxprime2)
print('There is',num_of_user_primes,'prime numbers between',usermaxprime2,'and',usermaxprime1)


# Answer the 3B questions below:
# 100th prime is: 541
# 2000th prime is: 17389
# Primes between 3000 and 30000:2815


# Write your Sundaram function below:
def sundaram(n):
    primes = list(range(1,n+1))
    for j in primes:
        i=1
        while i <= j:
            if (i + j + 2*i*j) in primes:
                primes.remove(i + j + 2*i*j)
            i += 1
    primes_new = [(2*i)+1 for i in primes]
    return(primes_new)
print('This will execute the Sieve of Sundaram, giving you a list of prime numbers between 3 and 2n.')
sund = int(input('Give a number:'))
print('The prime numbers between 3 and',(2*sund),'are',sundaram(sund))


###########
def eratosthenes(max_prime):
    primes = list(range(2,max_prime+1))
    for i in primes:
        j=2
        while i*j <= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j += 1
    return (primes)
eratosthenes1 = eratosthenes(288)
sundaram1 = [2] + sundaram(144)
print('If we take 144 for n then using the eratosthenes function and the sundaram function. We need to do 288 for the erastothenes function and 144 for the sundaram function and add 2 to the list. This should give the same answer.')
print(eratosthenes1)
print(sundaram1)

input('Press enter to exit:')
