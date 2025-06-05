import numpy as np 
#print(np.zeros(10))
#print(np.ones(10))
#print(np.ones(10)*5)
#print(np.arange(10,51,2))
#print(np.arange(0,9).reshape(3,3))
#print(np.eye(3,3))
import random as r 
#print(np.random.rand(1))
#print(np.random.rand(25))
#print(np.arange(1,101).reshape(10,10)/100)
#print(np.linspace(0.01,1,100).reshape(10,10))
arr= (np.arange(1,26).reshape(5,5))
print(arr)
print(arr[2:,1:])

print(arr[0:2,3:])
print(arr.sum())
print(arr.max())
print(arr.min())
print(arr.shape) 
print(arr.sum(axis=0))  # Sum along columns
print(arr.std() ) # Sum along rows