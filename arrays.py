from array import *

arr = array('i', [-1,2,3,4,5])
#print(arr)
#print(arr[2])

for i in arr:
    print(i)

for pnt in range(1,4):
    print(pnt, arr[pnt])

arr.reverse()
print(arr)