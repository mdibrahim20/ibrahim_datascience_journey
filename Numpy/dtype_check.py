# NumPy Data Types (dtype) & Type Conversion

''' NumPy arrays are faster than Python lists because they use fixed-size, homogeneous data types (All elements in a NumPy array must be of the same data type.).
This lets NumPy perform low-level optimizations in memory and speed.'''

import numpy as np

arr = np.array([1,2,3,4,5,6])
print(arr.dtype)

# Type Conversion
arr = np.array([1.4,2.4,3.5])
int_arr = arr.astype(int)
print(int_arr)


# Setting Type While Creating Array

arr2 = np.array([1,2,3,4,5,6],dtype='float64')
print(arr2)
print(arr2.dtype)


'''

Create an array [1.2, 3.4, 5.6] and check its dtype.

Convert it to integers using .astype(int).

Create a 2D array [[True, False], [False, True]] and check the dtype.

Convert [100, 200, 300] to float32 when creating the array.

Create a string array from ["apple", "banana", "cherry"] and check the dtype.


'''

a = np.array([1.2, 3.4, 5.6])
print(a.dtype)

print(a.astype(int))

boolArray = np.array([[True, False], [False, True]])
print(boolArray.dtype)

floatArray = np.array([100, 200, 300],dtype='float32')
print(floatArray)

stringArray = np.array(["apple", "banana", "cherry"])
print(stringArray.dtype)
