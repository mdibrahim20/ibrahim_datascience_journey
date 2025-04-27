'''
🎯 Real-World Scenario
You're working on simulations, data augmentation, or creating synthetic training data.
You need random numbers, controlled randomness (seeds), and normal distributions.
'''

import numpy as np

# --------------------------------------------
# rand(): Generates random numbers from a uniform distribution over [0, 1)
# Output: Random floats between 0 and 1
# Shape: (2, 3)
# --------------------------------------------
print("Uniform random numbers using rand():")
print(np.random.rand(2, 3))

# --------------------------------------------
# randn(): Generates random numbers from a standard normal distribution (mean=0, std=1)
# Output: Random floats around 0
# Shape: (2, 3)
# --------------------------------------------
print("\nStandard normal random numbers using randn():")
print(np.random.randn(2, 3))

# --------------------------------------------
# randint(): Generates random integers between low (inclusive) and high (exclusive)
# Output: Random integers from 0 to 99
# Shape: (2, 3)
# --------------------------------------------
print("\nRandom integers using randint():")
print(np.random.randint(0, 100, (2, 3)))

# --------------------------------------------
# seed(): Sets the random seed for reproducibility
# After setting a seed, random numbers will be the same every time you run the program
# --------------------------------------------
np.random.seed(2)
print("\nRandom numbers after setting seed:")
print(np.random.rand(2, 2))

# --------------------------------------------
# Simulating Normal Distribution Data:
# Generates data that follows a normal (Gaussian) distribution
# loc: mean of the distribution (center)
# scale: standard deviation (spread)
# size: number of samples
# --------------------------------------------
normal_data = np.random.normal(loc=170, scale=10, size=(1000,))
print("\nSimulated normal distribution data (first 10 values):")
print(normal_data[:10])  # Printing only first 10 values for readability

# --------------------------------------------
# Simulating Uniform Distribution Data:
# Generates random floats where every number between low and high is equally likely
# --------------------------------------------
uniform_data = np.random.uniform(low=0, high=100, size=(5,))
print("\nSimulated uniform distribution data:")
print(uniform_data)
