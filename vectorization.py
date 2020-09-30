# Import Libraries
import numpy as np
import time

# Test numpy Array
a = np.array([1,2,3,4])
print(a)

# Generate two vectors using numpy
a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time() # Time in
c = np.dot(a,b)
toc = time.time() # Time out

print(c)
print("Vectorized version took:" + str((toc-tic)) + "ms")

c=0

tic=time.time() # Time in
for i in range (1000000):
      c += a[i]*b[i]
toc=time.time() # Time out

print(c)
print("for loop took:" + str((toc-tic)) + "ms")

# Inference: numpy's dot method takes lesser time than bruteforce looping
