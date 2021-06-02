# import files here
from random import random , randint
import matplotlib.pyplot as plt
# 9 Ferns & Fractals

#(1)
iterations = 50000
#define x and y coordinates of 3
#vertices of triangle & aninitial point
x = [0.0,1.0,0.5,0.2]
y = [0.0,0.0,1.0,0.3]
r = 0.5
for i in range(iterations):
    p = randint(0,2)
    x.append(x[-1]*(1-0.5)+x[p]*0.5)
    y.append(y[-1]*(1-0.5)+y[p]*0.5)
plt.figure('Figure A')
plt.scatter(x,y,s=0.1)
plt.savefig('Chaos_game_triangle.png')



#(2)
def boxcounting(xlist,ylist,epsilon):

    from math import log

    # find min and max coordinates of the set
    xmin = min(xlist)
    xmax = max(xlist)
    ymin = min(ylist)
    ymax = max(ylist)

    # no. of boxes of side epsilon to cover whole set
    xcount = int((xmax-xmin)/epsilon)+1
    ycount = int((ymax-ymin)/epsilon)+1

    # initialise matrix of 0s, one entry per box
    check = [[0 for col in range(xcount)] for row in range(ycount)]

    # go through all points in set, if point in box ij, change matrix entry to 1
    for k in range(len(xlist)):
        i = int((xlist[k]-xmin)/epsilon)
        j = int((ylist[k]-ymin)/epsilon)
        check[j][i] = 1

    # count up all entries in matrix with entry 1
    boxcount=0
    for row in range(ycount):
        boxcount = boxcount+check[row].count(1)
    # return epsilon, N(epsilon), log(N)/log(1/epsilon)
    return log(1/epsilon),log(boxcount),log(boxcount)/log(1/epsilon)



#(3)
print(boxcounting(x,y,0.0625))



#(4)
epsilon = [1,1/0.5,1/0.25,1/0.125,1/0.0625]
boxcount = [3,6,14,38,110]
plt.figure('Figure B')
plt.loglog(epsilon,boxcount)
print('The estimate for the fractal dimension of the Sierpinski gasket is 1.585.')



#(5)
print('To make this estimate more accurate we could choose smaller values of epsilon and continue the curve on longer.')



