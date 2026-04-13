import numpy as np

# 1. datatype
array1 = np.array([[1,2,3,4],[5,6,0,0]])
print(type(array1))
print(array1.shape) # (rows,columns)
print(array1.size) # total element counts

# 1. list to numpy array 
arr = np.array([1,2,3,4,5])
print(arr)

# 2. numpy zeros
arr1 = np.zeros((3,3))
print(arr1)

# 3. numpy ones
arr2 = np.ones((3,3))
print(arr2)

# 4. numpy arrange - interval of digits (start,end-1,interval gap) an interval is optional
arr3 = np.arange(1,10,2)
print(arr3)

# 5. linspace - will take the random number of n digits between the start and the end the limit (eually spaced)
arr4 = np.linspace(1,2,5) # includes the end value
print(arr4)

# 6. Reshape array to the required dimension ( condition -> d * d = no of elements in the numpy array)
arr5 = np.array([1,2,3,4,5,6])
reshaped_numpy_arr = arr5.reshape((3,2))
print(reshaped_numpy_arr)

# 7. Element wise operation
a = np.array([1,2,3,4,5])
b = np.array([1,2,3,4,5])
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# 8. Methods
print(np.sum(a))
print(np.mean(a))
print(np.median(a))
print(np.min(a))
print(np.max(a))
print(np.sqrt(a))

# 9. Numpy Array Indexing
arr9 = np.array([1,2,3,4,5])
print(arr9[0])
print(arr9[2])

# 10. Numpy Array Slicing (statr:end-1)
arr10 = np.array([1,2,3,4,5,6,7])
print(arr10[0:4])
print(arr10[:])

# 11. Numpy Matrix Operation
matrix1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix2= np.array([[9,2,1],[7,4,1],[8,3,6]])
transposed_matrix = matrix1.T

sum = matrix1+matrix2
sub = matrix1-matrix2
mul = matrix1*matrix2
div = matrix1/matrix2

print(transposed_matrix)
print(sum)
print(sub)
print(mul)
print(div)

# 12. Scalar Addition
arr12 = np.array([[1,2,3],[4,5,6]])
scalar = 5
print(arr12+scalar)

#  13. Vecror Additon
arr13 = np.array([[1,2,3],[4,5,6]])
vector = np.array([1,2,3])
print(arr13+vector)

# 14. Aggregation function
arr14 = np.array([[1,2,3],[4,5,6]])
print(np.sum(arr14))
print(np.mean(arr14))
print(np.max(arr14))
print(np.min(arr14))
print(np.std(arr14))
print(np.sum(arr14,axis=1)) # sum of rows
print(np.sum(arr14,axis=0)) # sum of col

# 15. Random Array Generation
rand_array = np.random.rand(3,3)
print(rand_array)

# 16. Randome Array Generation within the range (n,m)
rand_array1 = np.random.randint(0,10,size=(3,3))
print(rand_array1)

# 17. Random seed. always the random numbers will be the same for every time running newly
# np.random.seed(42)

# 18. full
arr18 = np.full((5,4),1)
print(arr18)

# 19. eye (Indentity Matrix)
arr19 = np.eye(3)
print(arr19)

# 20. Analaysing Numpy Array
arr20 = np.array([[1,2,3,4],[2,3,4,5],[3,4,5,2]])
print(arr20.shape)
print(arr20.size)
print(arr20.ndim)
print(arr20.dtype)

# 21. np.full

arr20 = np.full((3,3),5)
print(arr20)

# 21 random
arr21 = np.random.randint((3,3))
print(arr21)

# 22 arrange

arr22 = np.arange(10,30,20)
print(arr22)