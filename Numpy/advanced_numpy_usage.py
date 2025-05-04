"""
🎯 Focus: Copy vs View, Memory Layout, Vectorization, and Performance Comparison

🎯 Real-World Scenario
You’re processing large image datasets or ML features (like 100,000 rows).
If you mistakenly use a view instead of a copy, changes can unintentionally affect your original data — or if you write loops instead of using vectorization, it could slow your code down 10–100x.

➡️ Learning these helps you:
➡️ Avoid memory bugs
➡️ Speed up computations
➡️ Understand what’s going on behind the scenes
"""

# ------------------- Copy Vs View -------------------------
# Copy creates a new array in memory
# View is just a different "lens" into the original data
# ----------------------------------------------------------
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
copy_arr = arr.copy()
view_arr = arr.view()

arr[0] = 99
print("Original:", arr)  # [99 2 3 4 5]
print("Copy:", copy_arr)  # [1 2 3 4 5] ✅
print("View:", view_arr)  # [99 2 3 4 5] ❌ (changed too!)


# ------------------- Memory Layout (C_CONTIGUOUS vs F_CONTIGUOUS) -------------------------
# C_CONTIGUOUS: Row-wise memory layout (default in Python)
# F_CONTIGUOUS: Column-wise (used in Fortran, MATLAB)
# ------------------------------------------------------------------------------------------

arr = np.array([[1, 2], [3, 4]])
print(arr.flags)  # Check memory layout
f_arr = np.asfortranarray(
    arr
)  #  Important in high-performance ML or Numba/Cython-based projects.
print(f_arr.flags)

# ------------------- Vectorization vs Loops -------------------------
# Vectorization:  no loops, faster operations with less code.
# Loops: Continuosuly iteration and slower due to time consuming.
# --------------------------------------------------------------------

# Slow method
lst = [1, 2, 3, 4, 5, 6]
double = [i * 2 for i in lst]
print(double)

# Fast NumPy metho
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr * 2)


# ------------------- Performance Comparison with timeit -------------
#  
# --------------------------------------------------------------------

import timeit

# Python list
list_time = timeit.timeit('''
lst = [i for i in range(1000)]
[i*2 for i in lst]
''', number=1000)

# NumPy array
array_time = timeit.timeit('''
import numpy as np
arr = np.arange(1000)
arr*2
''', number=1000)

print("List Time:", list_time)
print("NumPy Time:", array_time)
