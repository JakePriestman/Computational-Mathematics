# import files here
import matplotlib.pyplot as plt
import numpy as np
# 6A
#(i)
def Collatz(n):
    list = []
    if n == 1:
        list.append(1)
    while n > 1:
        list.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
    list.append(1)
    return list





#(ii)
#(a)
print('(ii)(a)')
print(Collatz(12))
#(b)
print('(ii)(b)')
print(Collatz(9))
#(c)
print('(ii)(c)')
print(Collatz(27))


#(iii)
def S(n):
    count = 0
    if n == 1:
        count += 1
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        count += 1
    count += 1
    return count

#(a)
print('(iii)(a)')
print(S(123))
#(b)
print('(iii)(b)')
print(S(901))
#(c)
print('(iii)(c)')
print(S(63728127))

#(iv)
n = np.arange(1,1000,1)
s = [S(i) for i in n]
plt.figure('Firgure A')
plt.title(' (iv) Plot of S(n) against n.')
plt.xlabel('n')
plt.ylabel('S(n)')
plt.plot(n,s,'o')

plt.figure('Firgure B')
plt.title('Logarithmic plot of S(n) against n.')
plt.xlabel('n')
plt.ylabel('S(n)')
plt.loglog(n,s,'o')


#(v)
def pert(n):
    mylist = list(range(1,n+1,1))
    for i in mylist:
        if S(i) >= i/10:
            mylist.remove(i)
    return((len(mylist)*100)/n)



#(vi)
def Collatz_max(n):
    list = []
    if n == 1:
        list.append(1)
    while n > 1:
        list.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
    list.append(1)
    return max(list)


Max = [Collatz_max(i) for i in n]
plt.figure('Firgure C')
plt.title('(vi) Plot of max(n) against n.')
plt.xlabel('n')
plt.ylabel('max(n)')
plt.plot(n,Max,'o')

plt.figure('Firgure D')
plt.title('Logarithmic plot of max(n) against n.')
plt.xlabel('n')
plt.ylabel('max(n)')
plt.loglog(n,Max,'o')
print('(vi) There is one maximum value that appears substanially more than other maximum values, which is only shown in the logarithmic plot.')


