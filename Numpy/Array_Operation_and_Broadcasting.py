"""
🔵 Topic: Array Operations & Broadcasting in NumPy
When working with data arrays in AI/ML (like user ratings, item features, preferences), speed and efficiency matter. That's where NumPy shines.

Think of every user or movie as a row of numbers (arrays) that describe them — we often need to:
Add two arrays together (e.g., user preferences + item features)
Scale features (e.g., normalize ratings)
Compute similarities (e.g., dot products, differences)
Summarize statistics (e.g., average, total, variance)

"""

# Element-wise Operations: These are basic math operations applied to each corresponding element of two arrays of the same shape. We can perform math directly on arrays.

import numpy as np

arr1 = np.array([10, 20, 30])
arr2 = np.array([40, 50, 60])

print(arr1 + arr2)
print(arr1 * arr2)
print(arr1 - arr2)
print(arr1 / arr2)
print(arr1**arr2)

# Broadcasting : Numpy's way of allowing Different shaped of arrays to be used together in operation without copying data.
# if we do math between two arrays that aren't the same shape, Numpy automatically strech the small one to match the larger one in a memory efficient way.

print("############### Broadcasting #################")
print(arr1 + 3)  # Add a scalar.
# Add rows to each row of a 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
new_row = np.array([7, 8, 9])
print("Broadcasting 2d: ", matrix + new_row)


""" 3. Aggregation Function: These functions summarize arrays.
    key functions: 
        -> sum() : total of all sum
        -> mean() : average value
        -> std() : standard deviation (how spread out)
        -> var() : variance (spread out)
        -> axis = 0 : column wise
        -> axis = 1 : row wise
"""
print("############## Aggregation ##############")
data = np.array([[80, 85, 90], [70, 75, 80], [90, 95, 100]])
print(np.sum(data))
print(np.mean(data))
print(np.std(data))
print(np.var(data))

# By Column or Row
print(np.sum(data,axis=0))
print(np.sum(data,axis=1))

# 4. Sorting, Searching, Counting: These are key tools for data analysis and preprocessing.

arr = np.array([10, 5, 8, 12])
print(np.sort(arr))
print(np.argmax(arr)) # Index of max value 
print(np.argmin(arr)) # Lowest or min index value
print(np.count_nonzero(arr>8)) # number of total values which are larger than 8


# Day 3 task:
# T1: Element-wise Operations
a1 = np.array([1,2,3])
a2 = np.array([4,5,6])

print(a1 + a2)  # [5 7 9]
print(a1 - a2)  # [-3 -3 -3]
print(a1 * a2)  # [4 10 18]
print(a1 / a2)  # [0.25 0.4  0.5 ]

# T2 : Broadcasting
mat33 = np.array([[[1,2,3],
                   [4,5,6],
                   [7,8,9]]])

d1_arr = np.array([1,1,1])
print(mat33 + d1_arr)

# T3: Aggregation
print(np.mean(mat33, axis=0))
print(np.mean(mat33, axis=1))



 
