#mapto3d.py
#an algorithm for importing and mapping 2D images to 3D plots
#Andrew Garcia, 2016
import numpy as np
import matplotlib.pyplot as plt
import pickle
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.image as mpimg

'converting image to code; in command line:'
#img1 = mpimg.imread("O36062_640.png")
#pickle.dump( img1, open( "jcskull.p", "wb" ) )

'loading encrypted image'
img1 = pickle.load( open( "jcskull.p", "rb" ),encoding='latin1')
'converting image to binary'
lum_img1 = img1[:,:,0]

'pixel dimensions (px x py)'

px=244
py=244


'''mapping algorithm: maps 2D binary image to 3D form by transforming relative
pixel color to depth'''

x=[]
y=[]

for i in range(py):
    for j in range(px):
        if lum_img1[i,j]<0.90:
            x.append(j)
            y.append(i)
z=1*np.ones(np.size(x))

x2=[]
y2=[]
          
for i in range(py):
    for j in range(px):
        if lum_img1[i,j]<0.80:
            x2.append(j)
            y2.append(i)
z2=2*np.ones(np.size(x2))

x3=[]
y3=[]

for i in range(py):
    for j in range(px):
        if lum_img1[i,j]<0.70:
            x3.append(j)
            y3.append(i)
z3=3*np.ones(np.size(x3))
            
x4=[]
y4=[]
            
for i in range(py):
    for j in range(px):
        if lum_img1[i,j]<0.60:
            x4.append(j)
            y4.append(i)
z4=4*np.ones(np.size(x4))

x5=[]
y5=[]
     
for i in range(py):
    for j in range(px):
        if lum_img1[i,j]<0.50:
            x5.append(j)
            y5.append(i)
z5=5*np.ones(np.size(x5))

x6=[]
y6=[]       
            
for i in range(py):
    for j in range(px):
        if lum_img1[i,j]<0.40:
            x6.append(j)
            y6.append(i)
z6=6*np.ones(np.size(x6))

x7=[]
y7=[]       
            
for i in range(py):
    for j in range(px):
        if lum_img1[i,j]<0.30:
            x7.append(j)
            y7.append(i)
z7=7*np.ones(np.size(x7))

x8=[]
y8=[]       
            
for i in range(py):
    for j in range(px):
        if lum_img1[i,j]<0.20:
            x8.append(j)
            y8.append(i)
z8=8*np.ones(np.size(x8))

x9=[]
y9=[]       
            
for i in range(py):
    for j in range(px):
        if lum_img1[i,j]<0.10:
            x9.append(j)
            y9.append(i)
z9=9*np.ones(np.size(x9))
            

fig = plt.figure()
ax = plt.axes(projection='3d') 
ax.plot(z,x,y,'o',color='magenta')
ax.plot(z2, x2, y2,'o',color='yellow')
ax.plot(z3, x3, y3,'o',color='black')
ax.plot(z4, x4, y4,'o',color='cyan')
ax.plot(z5,x5, y5,'o',color='pink')
ax.plot(z6,x6, y6,'o',color='magenta')
ax.plot(z7,x7, y7,'o',color='blue')
ax.plot(z8,x8, y8,'o',color='navy')
ax.plot(z9,x9, y9,'o',color='black')
plt.xlabel('')
plt.ylabel('')
plt.suptitle('Andrew R Garcia, 2016')
plt.show()
