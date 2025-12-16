import numpy as np

#from a python list
arr1=np.array([1,2,3,4,5])
print(arr1)

#multidimensional array
arr2=np.array([[1,2,3], [4,5,6]])
print(arr2)

print(arr2.shape)   #(rows, columns)
print(arr2.ndim)    #Number of dimensions
print(arr2.size)    #Total number of elements
print(arr2.dtype)   #Data type of elements

#vectorization


arr3= np.array([10,20,30,40])
arr4= np.array([100,110,120,130])
print(arr3 + arr4)
print (arr3*2)

#Universal functions
print(np.sqrt(arr3))    #array
print(np.exp(arr3))     #e^arr element-wise
print(np.sin(arr3))     #Sin of each elements

    #PRACTICE
arr5=np.array([2,4,6,8,10])
addition=np.sum(arr5)
print("SUM: ",sum)

print("MULTIPLICATION: ",arr5*5)

print("GREATER THAN 5: ", arr5[arr5>5])

