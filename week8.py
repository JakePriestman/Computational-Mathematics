## Save this file as userid_8.py where userid is *your* userid

## packages
from random import shuffle, random
from time import time, clock, perf_counter
import matplotlib.pyplot as plt

## functions

def selectionsort(mylist):
    sortedlist = []
    while len(mylist) > 0:
        lowest = mylist[0]
        for x in mylist:
            if x < lowest:
                lowest = x
        sortedlist.append(lowest)
        mylist.remove(lowest)
    return sortedlist

# add your bubblesort function for (3) here
def bubblesort(x):
    n = len(x)
    y = list(range(1,n))
    y.reverse()
    for i in y:
        for j in range(0,i):
            if x[j] > x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
    return(x)

# add the mergesort function (5) (download from Minerva) here
def mergesort(mylist):
    if len(mylist) <= 1:
        return mylist

    m = len(mylist) // 2
    l = mergesort(mylist[:m])
    r = mergesort(mylist[m:])

    result = []
    i = j = 0
    while (len(result)<len(r)+len(l)):
        if l[i] < r[j]:
            result.append(l[i])
            i = i+1
        else:
            result.append(r[j])
            j = j+1
        if i == len(l) or j == len(r):
            result.extend(l[i:] or r[j:])
            break
    return result
# Write the code described in (1) here
ivalues = []
sorttimelist = []
for i in range(1,11):
    ivalues.append(2**i)
    mylist = list(range(2**i))
    shuffle(mylist)
    time_start = perf_counter()
    selectionsort(mylist)
    time_end = perf_counter()
    sorttime = time_end-time_start
    sorttimelist.append(sorttime)

# Write the code to plot the graph for (2) here,
# and save it as userid_selection.png
plt.loglog(ivalues,sorttimelist)
plt.xlabel('2**i')
plt.ylabel('Time')
plt.savefig('201145579_selection.png')
# Write your answer for part (2) here
# (2)
print('The curve follows that of a quadrqatic curve. Therefore, the graph shows that the time selection sort takes to sort is directly proportional to the square of the size of the length of 2**i.')
# Write the code to plot the graph for (4) here
# and save it as userid_bubble.png
ivalues = []
sorttimelistbubble = []
for i in range(1,11):
    ivalues.append(2**i)
    mylist = list(range(2**i))
    shuffle(mylist)
    time_start = perf_counter()
    bubblesort(mylist)
    time_end = perf_counter()
    sorttime = time_end-time_start
    sorttimelistbubble.append(sorttime)
plt.loglog(ivalues,sorttimelistbubble)
plt.xlabel('2**i')
plt.ylabel('Time')
plt.savefig('201145579_bubble.png')

# Write the code to plot the graph for (5) here
# and save it as userid_merge.png
ivalues = []
sorttimelistmerge = []
for i in range(1,11):
    ivalues.append(2**i)
    mylist = list(range(2**i))
    shuffle(mylist)
    time_start = perf_counter()
    mergesort(mylist)
    time_end = perf_counter()
    sorttime = time_end-time_start
    sorttimelistmerge.append(sorttime)
plt.loglog(ivalues,sorttimelistmerge)
plt.xlabel('2**i')
plt.ylabel('Time')
plt.savefig('201145579_merge.png')

# Write the code for part (6) here
ivalues = []
sorttimelistpython = []
for i in range(1,11):
    ivalues.append(2**i)
    mylist = list(range(2**i))
    shuffle(mylist)
    time_start = perf_counter()
    mylist.sort()
    time_end = perf_counter()
    sorttime = time_end-time_start
    sorttimelistpython.append(sorttime)
plt.figure('Figure 2')
plt.loglog(ivalues,sorttimelistmerge)
plt.loglog(ivalues,sorttimelistpython)
plt.xlabel('2**i')
plt.ylabel('Time')
plt.savefig('201145579_merge.png')
# and give your answer below
# (6)
print('As shown by the second graph it is faster than the merge sort and the curve stays below the merge sort curve. Therefore, as 2**i increases the time it takes to sort the list ioncreases slower than for merge sort.')

# Write your improved implementation of bubblesort
# and give your answer below
# which recognizes an already sort list (part 7) here
# (7)
def bubblesortopt(x):
    n = len(x)-1
    swap = True
    while swap:
        swap = False
        for i in range(n):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
                swap = True
    return x
ivalues = []
sorttimelistbubbleopt = []
for i in range(1,11):
    ivalues.append(2**i)
    mylist = list(range(2**i))
    shuffle(mylist)
    mergesort(mylist)
    time_start = perf_counter()
    bubblesortopt(mylist)
    time_end = perf_counter()
    sorttime = time_end-time_start
    sorttimelistbubbleopt.append(sorttime)
plt.figure('Figure 3')
plt.loglog(ivalues,sorttimelistbubbleopt)
plt.xlabel('2**i')
plt.ylabel('Time')
print('As you can see from the graph the line represents a linear relationship between time and 2**i.')
# Write the code for part (8) here
# and give your answer below
# (8)
def checksort(n):
    mylist = n
    shuffle(mylist)
    while sorted(mylist) != mylist:
        shuffle(mylist)
        if sorted(mylist) == mylist:
            break
    return mylist

ivalues = []
sorttimelistchecksort = []
for i in range(1,10):
    ivalues.append(i)
    mylist = list(range(i))
    time_start = perf_counter()
    checksort(mylist)
    time_end = perf_counter()
    sorttime = time_end-time_start
    sorttimelistchecksort.append(sorttime)
plt.figure('Figure 4')
plt.loglog(ivalues,sorttimelistchecksort)
plt.xlabel('i')
plt.ylabel('Time')
print('As the length of the list increases the time is takes to sort stays similar for smaller lengths of the list and then rapidly increases in time at a particular length of list.')
