import numpy as np
print("INDEXING:")
arr=np.array([10,20,30,40,50])

#Indexing
print(arr[0])   #10
print(arr[1])   #20
print(arr[2])   #30
print(arr[3])   #40
print(arr[4])   #50
print(arr[-1])  #Printing the last element
print(arr[-5])  #Printing the elements backward

#2D array indexing(rows,columns)
print("2D ARRAY INDEXING:")
arr2=np.array([
    [1,2,3],
    [4,5,6]
])
print(arr2[0,1])    #2
print(arr2[0,2])    #3
print(arr2[1,2])    #6

#1D SLICING
print("1D SLICING:")

arr3=np.array([100,200,300,400,500,600,700,800,900,1000])
print(arr3[0:5])    #[100-500]
print(arr3[5:10])   #[600-1000]
print(arr3[2::])    #start from [300...]
print(arr3[::-1])   #reverse

#2D SLICING
print("2D SLICING:")
print(arr2[:,1])    #Everything in rows, column 1=[2,5]
print(arr2[0,:])    #Everything in columns, row 0=[1,2,3]

#BOOLEAN INDEXING (selecting by condtion)
arr4=np.array([2,4,5,8,10,12,14,16,18,20,22,24,26,28,30,32])
print(arr4[arr4>18])    #Greater than 18
print(arr4[arr4<24])    #Less than 24
print(arr4.size)        #Total number of elements
total=np.sum(arr4)      #Sum of elements
print(total)

#RESHAPING
print("RESHAPING: ")
reshaped=arr4.reshape(4,4)     #reshaping[4rows,4column]
print(reshaped)

#RESHAPING ARRAYS(flatten)
print("FLATTEN: ")
flat=arr2.flatten()     #Turning arr2 into 1D.
print(flat)

#RANDOM NUMBER GENERATION
print("RANDOMIZE: ")
rand_arr=np.random.randint(1,1000,size=5)   #print 5 random numbers in a dimention
print(rand_arr)

rand2d=np.random.rand(3,3)
print(rand2d)
rand2d_int=np.random.randint(1,10,size=(2,3))
print(rand2d_int)

#EXERCISE
print("EXERCISE: ")
exe=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
exe_reshape=exe.reshape(3,4)
print("RESHAPE:",exe_reshape)
print("FIRST ROW",exe_reshape[0,:])
print("LAST COLUMN",exe_reshape[:,-1])
print("GREATER THAN",exe[exe>6])
