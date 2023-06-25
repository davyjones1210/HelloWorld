import numpy as np

a=np.array([1,2,3])
print(type(a))

import time
import sys
b=range(1000)
print(sys.getsizeof(5)* len(b))

c=np.arange(1000)
print(c.size*c.itemsize)

size = 100000
L1 = range(size)
L2 = range(size)
A1 = np.arange(size)
A2= np.arange(size)

start = time.time()
result = [(x+y) for x,y in zip(L1,L2)]
#print(result)
#print("Python list took: ", (time.time() - start)*1000)
start = time.time()
result = A1+A2
#print("Numpy array took: ", (time.time() - start)*1000)

a=np.array([[1,2],[3,4],[5,6]])
#print(a)
#print(a.ndim)
#print(a.itemsize)
#print(a.shape)
a=np.array([[1,2],[3,4],[5,6]], dtype=np.float64)
print(a)
print(a.itemsize)
print(a.shape)
a=np.array([[1,2],[3,4],[5,6]], dtype=complex)
# print(a)
# print(type(a))
# print(a.itemsize)
# print(a.shape)
# print(np.zeros((3,4)))
# print(np.ones((3,4)))
l=range(5)
#print(l)
l=np.arange(5)
#print(l)
print('concatentation example: ')
print(np.char.add(['hello', 'hi'], ['abc','xyz']))
#print(np.char.multiply('Hello ', 20))
print(np.char.center('Hello', 20, fillchar = '-'))
print(np.char.capitalize('hello world'))
print(np.char.title('how are you doing?'))
print(np.char.lower(['HELLO','WORLD']))
print(np.char.lower('HELLO'))
print(np.char.upper(['python','data']))
print(np.char.upper('python is easy'))
print(np.char.split('are you coming to the party?'))
print(np.char.splitlines('hello\nhow are you?'))
print(np.char.strip(['nina','admin','anaita'], 'a'))
print(np.char.join([':','-'],['dmy','ymd']))
print(np.char.replace('He is a good dancer', 'is', 'was'))
