#Pandas Tutorial
import pandas as pd
print(pd.__version__)
#Series create, manipulate, querry, delete
#Creating a series from a list
arr = [0,1,2,3,4]
s1=pd.Series(arr)
print(s1)
order = [1,2,3,4,5]
s2 = pd.Series(arr, index=order)
print(s2)

import numpy as np
n=np.random.randn(5) #create a random ndarray
print(n)
#print(type(n))
index = ['a','b','c','d','e']
s2 = pd.Series(n,index = index)
print(s2)

#Create a series from dictionary
d = {'a':1,'b':2,'c':3,'d':4,'e':5}
s3=pd.Series(d)
print(s3)

#You can modify the index of Series
print(s1)
s1.index=['A','B','C','D','E']
print(s1)

#Slicing
a=s1[:3]
print(a)
s4=s1._append(s3)
print(s4)
print(s4.drop('e'))
print(s4)

#Series operations
arr1=[0,1,2,3,4,5,7]
arr2=[6,7,8,9,5]
s5=pd.Series(arr2)
print(s5)
s6=pd.Series(arr1)
print(s6)
print(s5.add(s6))
print(s5.sub(s6))
s7=s5.mul(s6)
print(s7)
#print(s5.div(s6))
print("Median: ", s7.median())
print("Max: ", s7.max())
print("Min: ", s7.min())
