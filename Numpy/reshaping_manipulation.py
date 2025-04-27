"""
This is like playing with Lego bricks for arrays – you’ll reshape, flatten, split, and merge arrays to prep them for machine learning models, visualizations, and more!

🎯 Real-World Scenario
You’re working with image data in machine learning.
An image comes in as a 3D array (height, width, channels).
But your model expects a 2D matrix (samples, features).

💡 You’ll need to reshape, flatten, and transpose these arrays effectively.

"""

import numpy as np

# reshape() : it will reshape the existing matrix.
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(a.reshape(2, 5))


# flatten():
# It always returns a new copy of the array, fully independent.
# It turns the array into a 1D array.
# Memory is different, and changes in the new array do NOT affect the original array.

# ravel():
# It tries to return a view (not a copy) of the existing array.
# It also turns the array into a 1D array.
# Memory and data stay the same (if possible).
# Changes in the new array can affect the original array.

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.flatten())
print(b.ravel())

# transpose() or .T :
# Both are used to swap the rows and columns of a matrix (2D array).
# a.transpose() and a.T do the same thing — they return a transposed view of the array (without changing the original unless you assign it).

c = np.array([[11, 12, 13], [14, 15, 16]])
print(c.transpose())
print(c.T)


# concatenate():
# Joins two or more arrays **along an existing axis**.
# It needs the shapes to match, except in the axis you are joining.

# stack():
# Joins arrays **along a new axis**.
# It *adds* an extra dimension to glue them together.


a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(np.concatenate((a, b), axis=1))
print(np.stack((a, b)))
print(np.vstack((a, b)))
print(np.hstack((a, b)))

# split():
# Breaks an array into multiple sub-arrays **along an axis**.
# It’s like slicing a big cake into several smaller pieces.

arr = np.array([10, 20, 30, 40, 50, 60])
print(np.split(arr, 3))

# Tasks:
oneD = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
twoD = oneD.reshape(3,4)
print(twoD)
print(twoD.flatten())
secondTwoD = np.array([[1, 2], [3, 4]])
print(secondTwoD.T)
x = np.array([[1, 2]])
y = np.array([[3, 4]])
print(np.vstack((x, y)))
print(np.hstack((x, y)))

arr = np.array([10, 20, 30, 40, 50, 60])
print(np.split(arr,3))
