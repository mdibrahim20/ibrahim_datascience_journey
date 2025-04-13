import numpy as np

# 1. np.array() : Create array from python list or tuples

a = np.array([1,2,3,4])
b = np.array([[1,2,3],[4,5,6]])

print("1D array:",a)
print("2D array:",b)

# 2. np.arange(start, stop, step): Like Python’s range(), but returns a NumPy array.

arr = np.arange(0,10,2)
print("Arange",arr)

# 3. np.zeros(shape) : Creates an array filled with 0

z = np.zeros((2,3))
print("Zeros",z)

# 4. np.ones(shape):  Creates an array filled with 1.

o = np.ones((3,4))
print("Ones",o)

# 5. np.full(shape, fill_value): Creates an array filled with any value you want.

f = np.full((3,3),7)
print("Full",f)

# 6. np.linspace(start, stop, num):  Returns num evenly spaced values between start and stop.

ls = np.linspace(0,10,3)
print(ls)

'''
Exercies:
Create a 1D array from 1 to 10 using arange().

Create a 3x3 array of all 1s.

Create a 2x4 array filled with the number 99.

Generate 6 evenly spaced numbers from -1 to 1 using linspace().

Create a 2D array from a list of lists: [[5, 10], [15, 20]].
'''

oneD = np.arange(1,11,1)
print(oneD)

onesArray = np.ones((3,3))
print(onesArray)

filledWith = np.full((2,4),99)
print(filledWith)

linspace = np.linspace(-1,1,6)
print(linspace)

twoD = np.array([[5,10],[15,20]])
print(twoD)