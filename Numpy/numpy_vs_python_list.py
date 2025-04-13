import numpy as np
import time

# python list and numpy array

py_list = list(range(10000000))
np_array = np.arange(10000000)

start = time.time()
py_list_result = [x+1 for x in py_list]
print("Python List Time:",time.time()-start)

# Numpy array addition
start = time.time()
np_result = np_array+1
print("Numpy Array Time:",time.time()-start)
