'''
Suppose you're building a machine learning model to predict flight delays.
You need to scale features (normalize) using math functions like logarithms, or adjust sensor data using trigonometric transformations.

'''

import numpy as np;

# Trigonometric Function
angles = np.array([0,np.pi/2,np.pi])
print(np.sin(angles))
print(np.cos(angles))
print(np.tan(angles))

# Exponential and Logarithmic Functions
values = np.array([1,2,3])
print(np.exp(values))
print(np.log(values))
print(np.log10(values))

# Rounding Functions
nums = np.array([1.2,2.5,3.7])
print(np.floor(nums))
print(np.ceil(nums))
print(np.round(nums))