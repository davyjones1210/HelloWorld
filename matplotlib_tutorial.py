#MATPLOTLIB Tutorial
from matplotlib import pylab
print(pylab.__version__)
#Use Numpy to generate random data
import numpy as np
x=np.linspace(0,10,25)
y = x*x+2
# print(x)
# print(y)
#print(np.array([x,y]).reshape(25,2).reshape(2,25))
#It only takes 1 command to draw
#pylab.plot(x,y,'r')     # r stands for red, b for blue
#pylab.show()
#Drawing a subgraph
# pylab.subplot(1,2,1)     #The contents of the brackets represent (rows, colmns, indexes)
# pylab.plot(x,y,'r--')
# pylab.subplot(1,2,2)
# pylab.plot(y,x,'g--')
#pylab.show()
from matplotlib import pyplot as plt
fig = plt.figure()
axis = fig.add_axes([0.5,0.1,0.8,0.8])   #control the left, bottom, width, heighe of the canvas (from 0 to 1)
axis.plot(x,y,'r')
#plt.show()

fig,axes = plt.subplots(nrows = 1, ncols = 2)    #submap is of 1 row, 2 columns
for ax in axes:
    ax.plot(x,y,'r')
    plt.show()

    