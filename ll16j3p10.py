# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 12:07:07 2018

@author: jakei
"""
import numpy
import matplotlib.pyplot as plt
import matplotlib.cm as cm

print('For my project, I am going to explore Julia sets and the patterns created by plotting them. Julia sets are sets named after the French mathematician Gaston Julia. The sets are defined by an initial set of z_0s which produce a bounded sequence {z_n} when z_(n+1)=f(z)=(z_n)^2+C is iterated for complex constant C. I will be investigating the different properties of the sets and how changing values for C or the iterating relation affects the outputted patterns. Furthermore, I will be examining at the Mandlebrot set and I will look at the fractal dimensions of my Julia sets.')
#Plot c=-1 Re(z)=[-2,2] and Im(z)=[-1,1]
print(' ')
print('The plot below is of a Julia set with C=-1 and Re(z)=[-2,2] and Im(z)=[-1,1]. When you iterate (z_n)^2 -1, starting with zero, the values are only ever -1 or 0. This means the Julia plot is symmetrical about the origin. The white parts of the graph indicate where |z_n| is bounded by 2 and the black parts indicate the parts that get larger than 2.')
#Image width and height
imag_width, imag_height = 500, 500
#c Value
c = complex(-1,0)
zabs_max = 4
nit_max = 1000
#Real bounds
re_min, re_max = -2.0, 2.0
re_width = re_max - re_min
#Imaginary bounds
im_min, im_max = -1.0, 1.0
im_height = im_max - im_min
#initial set of z_0's
count = 0
julia = numpy.zeros((imag_width, imag_height))
for re in range(imag_width):
    for im in range(imag_height):
        nit = 0
        #Map pixel position to a point in the complex plane
        z = complex(re / imag_width * re_width + re_min,
                    im / imag_height * im_height + im_min)
        #iterations
        while abs(z) <= zabs_max and nit < nit_max:
            z = z**2 + c
            nit += 1
        ratio = nit / nit_max
        julia[re,im] = ratio
        if abs(z) <= zabs_max:
            count +=1
            
print('The Fractal dimension of this plot is',numpy.log(250000-count)/(numpy.log(count)-1.18509))
plt.figure(dpi=100)
plt.title('Julia set of C = -1.')
plt.imshow(julia.T,cmap='hot', interpolation='bilinear',extent=[-2,2,-1,1])
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()



print('If we change C=0, then the Julia set becomes the unit circle. This is because if we take a number n such that n<1, then upon squaring, it will keep getting smaller and is hence bounded by the unit circle. If we take n>1, then upon squaring, it will keep increasing and hence gets infinitely large.')
#Explore different values of C and plot other Julia sets and change polynomial f and look at behaviour (disjoint or joint plots)
#Image width and height
imag_width, imag_height = 500, 500
#c Value
c = 0
zabs_max = 4
nit_max = 1000
#Real bounds
re_min, re_max = -2.0, 2.0
re_width = re_max - re_min
#Imaginary bounds
im_min, im_max = -1.0, 1.0
im_height = im_max - im_min
#initial set of z_0's
count = 0
julia = numpy.zeros((imag_width, imag_height))
for re in range(imag_width):
    for im in range(imag_height):
        nit = 0
        #Map pixel position to a point in the complex plane
        z = complex(re / imag_width * re_width + re_min,
                    im / imag_height * im_height + im_min)
        #iterations
        while abs(z) <= zabs_max and nit < nit_max:
            z = z**2 + c
            nit += 1
        ratio = nit / nit_max
        julia[re,im] = ratio
        if abs(z) <= zabs_max:
            count +=1

print('The Fractal dimension of this plot is',numpy.log(250000-count)/numpy.log((count)))
plt.figure(dpi=100)
plt.title('Julia set of C = 0')
plt.imshow(julia.T,cmap='hot', interpolation='bilinear',extent=[-2,2,-1,1])
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()
print('As the real part of C gets closer to zero it gets closer to the unit circle. If we change C to a complex number with an imaginary part close to 0 but real part closer to -1, it produced a different pattern. This is where C=-0.79+0.15i.')



#Image width and height
imag_width, imag_height = 500, 500
#c Value
c = complex(-.79,0.15)
zabs_max = 4
nit_max = 1000
#Real bounds
re_min, re_max = -2.0, 2.0
re_width = re_max - re_min
#Imaginary bounds
im_min, im_max = -1.0, 1.0
im_height = im_max - im_min
#initial set of z_0's
julia = numpy.zeros((imag_width, imag_height))
for re in range(imag_width):
    for im in range(imag_height):
        nit = 0
        #Map pixel position to a point in the complex plane
        z = complex(re / imag_width * re_width + re_min,
                    im / imag_height * im_height + im_min)
        #iterations
        while abs(z) <= zabs_max and nit < nit_max:
            z = z**2 + c
            nit += 1
        ratio = nit / nit_max
        julia[re,im] = ratio
        
plt.figure(dpi=100)
plt.title('Julia set of C = -0.79+0.15*i')
plt.imshow(julia.T,cmap='cubehelix', interpolation='bilinear',extent=[-2,2,-1,1])
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()
print('As the imaginary part of C gets closer to zero and the real part gets closer to 1 the fractal patterns become thinner and straighter. It follows along the real and imaginary axis. As seen in the plot below.')



#Image width and height
imag_width, imag_height = 500, 500
#c Value
c = complex(-1.476,0)
zabs_max = 4
nit_max = 1000
#Real bounds
re_min, re_max = -2.0, 2.0
re_width = re_max - re_min
#Imaginary bounds
im_min, im_max = -1.0, 1.0
im_height = im_max - im_min
#initial set of z_0's
count = 0
julia = numpy.zeros((imag_width, imag_height))
for re in range(imag_width):
    for im in range(imag_height):
        nit = 0
        #Map pixel position to a point in the complex plane
        z = complex(re / imag_width * re_width + re_min,
                    im / imag_height * im_height + im_min)
        #iterations
        while abs(z) <= zabs_max and nit < nit_max:
            z = z**2 + c
            nit += 1
        ratio = nit / nit_max
        julia[re,im] = ratio
        if abs(z) <= zabs_max:
            count +=1
            
print('The Fractal dimension of this plot is',numpy.log(250000-count)/numpy.log((count)))
plt.figure(dpi=100)
plt.title('Julia set of C = -1.476')
plt.imshow(julia.T,cmap='bone', interpolation='bilinear',extent=[-2,2,-1,1])
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()
print('If we change the polynomial f, then the amount of outward fractal spikes change. For example, for z^2 we have two outward fractal spikes and if it was z^3 then it would produce three and so on respectively. This is very interesting as it can make some very fascinating Julia plots. Here are three plots for z^3, z^4 and z^6. As you can see the pattern follows.')



#Image width and height
imag_width, imag_height = 500, 500
#c Value
c = complex(-.79,0.15)
zabs_max = 4
nit_max = 1000
#Real bounds
re_min, re_max = -2.0, 2.0
re_width = re_max - re_min
#Imaginary bounds
im_min, im_max = -1.0, 1.0
im_height = im_max - im_min
#initial set of z_0's
julia = numpy.zeros((imag_width, imag_height))
for re in range(imag_width):
    for im in range(imag_height):
        nit = 0
        #Map pixel position to a point in the complex plane
        z = complex(re / imag_width * re_width + re_min,
                    im / imag_height * im_height + im_min)
        #iterations
        while abs(z) <= zabs_max and nit < nit_max:
            z = z**3 + c
            nit += 1
        ratio = nit / nit_max
        julia[re,im] = ratio
        if abs(z) <= zabs_max:
            count +=1
            
print('The Fractal dimension of this plot is',numpy.log(250000-count)/numpy.log((count)))
plt.figure(dpi=100)
plt.title('Julia set of C = -0.79+0.15*i and z^3')
plt.imshow(julia.T,cmap='cubehelix', interpolation='bilinear',extent=[-2,2,-1,1])
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()



#Image width and height
imag_width, imag_height = 500, 500
#c Value
c = complex(-.79,0.15)
zabs_max = 4
nit_max = 1000
#Real bounds
re_min, re_max = -2.0, 2.0
re_width = re_max - re_min
#Imaginary bounds
im_min, im_max = -1.0, 1.0
im_height = im_max - im_min
#initial set of z_0's
julia = numpy.zeros((imag_width, imag_height))
for re in range(imag_width):
    for im in range(imag_height):
        nit = 0
        #Map pixel position to a point in the complex plane
        z = complex(re / imag_width * re_width + re_min,
                    im / imag_height * im_height + im_min)
        #iterations
        while abs(z) <= zabs_max and nit < nit_max:
            z = z**4 + c
            nit += 1
        ratio = nit / nit_max
        julia[re,im] = ratio
        if abs(z) <= zabs_max:
            count +=1
            
print('The Fractal dimension of this plot is',numpy.log(250000-count)/numpy.log((count)))
plt.figure(dpi=100)
plt.title('Julia set of C = -0.79+0.15*i and z^4')
plt.imshow(julia.T,cmap='cubehelix', interpolation='bilinear',extent=[-2,2,-1,1])
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()



#Image width and height
imag_width, imag_height = 500, 500
#c Value
c = complex(-.79,0.15)
zabs_max = 4
nit_max = 1000
#Real bounds
re_min, re_max = -2.0, 2.0
re_width = re_max - re_min
#Imaginary bounds
im_min, im_max = -1.0, 1.0
im_height = im_max - im_min
#initial set of z_0's
julia = numpy.zeros((imag_width, imag_height))
for re in range(imag_width):
    for im in range(imag_height):
        nit = 0
        #Map pixel position to a point in the complex plane
        z = complex(re / imag_width * re_width + re_min,
                    im / imag_height * im_height + im_min)
        #iterations
        while abs(z) <= zabs_max and nit < nit_max:
            z = z**6 + c
            nit += 1
        ratio = nit / nit_max
        julia[re,im] = ratio
        if abs(z) <= zabs_max:
            count +=1
            
print('The Fractal dimension of this plot is',numpy.log(250000-count)/numpy.log((count)))
plt.figure(dpi=100)
plt.title('Julia set of C = -0.79+0.15*i and z^6')
plt.imshow(julia.T,cmap='cubehelix', interpolation='bilinear',extent=[-2,2,-1,1])
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()
print('There are different types of Julia sets in which some are connected throughout and others are disconnected. The difference between the two is the value of C. A Julia set with a value of C that is definitely in the Mandlebrot set (this will be discussed further below) is said to be connected. A connected Julia set looks like this;')



#Image width and height
imag_width, imag_height = 500, 500
#c Value
c = complex(-.52,0.57)
zabs_max = 4
nit_max = 1000
#Real bounds
re_min, re_max = -2.0, 2.0
re_width = re_max - re_min
#Imaginary bounds
im_min, im_max = -1.0, 1.0
im_height = im_max - im_min
#initial set of z_0's
count = 0
julia = numpy.zeros((imag_width, imag_height))
for re in range(imag_width):
    for im in range(imag_height):
        nit = 0
        #Map pixel position to a point in the complex plane
        z = complex(re / imag_width * re_width + re_min,
                    im / imag_height * im_height + im_min)
        #iterations
        while abs(z) <= zabs_max and nit < nit_max:
            z = z**2 + c
            nit += 1
        ratio = nit / nit_max
        julia[re,im] = ratio
        if abs(z) <= zabs_max:
            count +=1
            
print('The Fractal dimension of this plot is',numpy.log(250000-count)/numpy.log((count)))
plt.figure(dpi=100)
plt.title('Connected Julia set of C = -0.52+0.57*i')
plt.imshow(julia.T,cmap='hot', interpolation='bilinear',extent=[-2,2,-1,1])
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()
print('A Julia set with a value of C that is definitely not in the Mandlebrot set is said to be disconnected. An example of this is;')



#Image width and height
imag_width, imag_height = 500, 500
#c Value
c = complex(0,0.66)
zabs_max = 4
nit_max = 1000
#Real bounds
re_min, re_max = -2.0, 2.0
re_width = re_max - re_min
#Imaginary bounds
im_min, im_max = -1.0, 1.0
im_height = im_max - im_min
#initial set of z_0's
julia = numpy.zeros((imag_width, imag_height))
for re in range(imag_width):
    for im in range(imag_height):
        nit = 0
        #Map pixel position to a point in the complex plane
        z = complex(re / imag_width * re_width + re_min,
                    im / imag_height * im_height + im_min)
        #iterations
        while abs(z) <= zabs_max and nit < nit_max:
            z = z**2 + c
            nit += 1
        ratio = nit / nit_max
        julia[re,im] = ratio
            
plt.figure(dpi=100)
plt.title('Disconnected Julia set of C = -0.79+0.15*i')
plt.imshow(julia.T,cmap='magma', interpolation='bilinear',extent=[-2,2,-1,1])
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()

print('I have estimated the fractal dimension by counting the number of pixels in each plot where |z_n|≥ 4, that is all the pixels that are unbounded. I have taken the log of the unbounded pixels and divided by the log of the pixels that remain bounded.')

#Plot Mandlebrot set for f
print('Arguably, the most famous Julia set is the Mandlebrot set. The Mandlebrot set is the set of C’s for which z_n^2  + C does not diverge. That being z_n^2  + C is bounded in absolute value. This plot looks like this;')
def mandlebrot(re,im,max_it):
    c = complex(re,im)
    z = 0.0
    
    for i in range(max_it):
        z = z**2 + c
        if (z.real**2 + z.imag**2) >= 4:
            return i
    return max_it


columns = 500
rows = 500

result = numpy.zeros([rows,columns])
#real axis
for row_index, re in enumerate(numpy.linspace(-2,1,num=rows)):
    for column_index, im in enumerate(numpy.linspace(-1,1,num=columns)):
        result[row_index,column_index] = mandlebrot(re,im,100)

plt.figure(dpi=100)
plt.title('The Mandlebrot Set')
plt.imshow(result.T,cmap='CMRmap', interpolation='bilinear',extent=[-2,1,-1,1])
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()

print('The Mandlebrot set is very interesting as you can approximate π using it. At the cusp of the main cardiod of the Mandlebrot set, shown by the arrow, C=1/4 here. So, if we take C=1/4+ϵ, where ϵ is an arbitrarily small positive quantity, then as ϵ gets smaller and smaller, the number of iterations it takes for C to become greater than 2, N(C), gets larger. Here is a table showing this.')

columns = 500
rows = 500

result = numpy.zeros([rows,columns])
#real axis
for row_index, re in enumerate(numpy.linspace(-2,1,num=rows)):
    for column_index, im in enumerate(numpy.linspace(-1,1,num=columns)):
        result[row_index,column_index] = mandlebrot(re,im,100)

plt.figure(dpi=100)
plt.title('The Mandlebrot Set')
ax = plt.axes()
ax.arrow(0, 0, 0.25, 0, head_width=0.05, head_length=0.05, fc='k', ec='k')
plt.imshow(result.T,cmap='CMRmap', interpolation='bilinear',extent=[-2,1,-1,1])
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()

mylist = [['1       ','1.25    ','2   '],
          ['0.01    ','0.26    ','30  '],
          ['0.0001  ','0.2501  ','312 '],
          ['0.000001','0.250001','3140']]

print(': Epsilon    : C          : N(C)   :')

for item in mylist:
    print(':',item[0],' ',':',
          item[1],' ',':',
          item[2],' ',':')

print('As you can see from the table, the number of iterations N(C) increases but starts to look like π. If you now place a decimal point in the right place you start to get an approximation for π. However, this is an extremely inefficient way of approximating π.')
mylist2 = [['1       ','1.25    ','2    '],
          ['0.01    ','0.26    ','3.0  '],
          ['0.0001  ','0.2501  ','3.12 '],
          ['0.000001','0.250001','3.140']]

print(': Epsilon    : C          : N(C)    :')

for item in mylist2:
    print(':',item[0],' ',':',
          item[1],' ',':',
          item[2],' ',':')
#Plot with bounded black
print('The next plot is a version of famous Julia sets called a Douady Rabbit. A Douady rabbit is one a various Julia sets with C close to the centre period of 3 buds. In this plot,, the black represents the parts that are bounded and the red shows that parts that are unbounded.')
#Image width and height
imag_width, imag_height = 500, 500
#c Value
c = complex(-.12,0.75)
zabs_max = 4
nit_max = 1000
#Real bounds
re_min, re_max = -2.0, 2.0
re_width = re_max - re_min
#Imaginary bounds
im_min, im_max = -1.0, 1.0
im_height = im_max - im_min
#initial set of z_0's
count = 0
julia = numpy.zeros((imag_width, imag_height))
for re in range(imag_width):
    for im in range(imag_height):
        nit = 0
        #Map pixel position to a point in the complex plane
        z = complex(re / imag_width * re_width + re_min,
                    im / imag_height * im_height + im_min)
        #iterations
        while abs(z) <= zabs_max and nit < nit_max:
            z = z**2 + c
            nit += 1
        ratio = nit / nit_max
        julia[re,im] = ratio
        if abs(z) <= zabs_max:
            count +=1
            
print('The Fractal dimension of this plot is',numpy.log(250000-count)/numpy.log((count)))
plt.figure(dpi=100)
plt.title('The Douady Rabbit')
plt.imshow(julia.T,cmap='RdGy', interpolation='bilinear',extent=[-2,2,-1,1])
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()

print('Throughout my investigation of Julia sets, I have gained a lot of insight into how they work and why they are important in Mathematics, from the fractal patterns having uses in mobile phones to their use to approximate π. I have found what different types of Julia sets there are and what makes a connected or disconnected Julia set. I have learned the importance of the value of C and the polynomial f in regards to the fractal pattern that is outputted by the Julia set. Furthermore, I have investigated the importance of the Mandlebrot set and how it can be used to approximate π.')