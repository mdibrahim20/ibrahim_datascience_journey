# NumPy Learning Notes 📘

This folder contains my notes, exercises, and examples as I revisit and master NumPy for data science and machine learning.

## ✅ Topics Covered (0 ➡️ Hero)

### 🟢 Basics & Fundamentals

- What is NumPy and Why Use It?
- Installing and Importing NumPy
- NumPy Arrays vs Python Lists
- Array Creation Methods:
  - `array()`, `arange()`, `zeros()`, `ones()`, `linspace()`, `full()`
- Data Types (`dtype`) and Type Conversion

### 🟡 Indexing, Slicing & Iteration

- 1D, 2D, and 3D Array Indexing
- Fancy Indexing & Boolean Indexing
- Conditional Selection
- Iterating Through Arrays Efficiently

### 🔵 Array Operations

- Element-wise Operations
- Broadcasting
- Aggregation: `sum()`, `mean()`, `std()`, `var()`, etc.
- Sorting, Searching, Counting

### 🔴 Reshaping & Manipulation

- Reshape, Flatten, Ravel
- Transpose, Axis swapping
- Concatenate, Stack, Split

### 🟣 Mathematical Functions

- Trigonometric, Exponential, Logarithmic functions
- Rounding: `floor()`, `ceil()`, `round()`

### 🟠 Random Module (Very Important!)

- `rand()`, `randn()`, `randint()`
- Reproducibility with `seed()`
- Simulating Data with Normal/Uniform Distribution

### 🟤 Advanced Usage

- Copy vs View
- Memory Layout (`C_CONTIGUOUS` vs `F_CONTIGUOUS`)
- Vectorization vs For-Loops
- Performance Comparisons (with `timeit`)

### 🧪 Real-World Applications

- Image Data Handling
- Data Preprocessing
- Matrix Operations in ML
- Efficient Feature Calculations

## 📂 Structure

| File                        | Description                             |
| --------------------------- | --------------------------------------- |
| `array_basics.py`           | Creating and exploring arrays           |
| `slicing_examples.py`       | Indexing and slicing arrays             |
| `operations_demo.py`        | Element-wise operations                 |
| `reshaping.py`              | Reshape and array manipulation          |
| `random_usage.py`           | Using NumPy's random module             |
| `performance_comparison.py` | NumPy vs Python lists                   |
| `notebook.ipynb`            | Jupyter notebook for notes and practice |

## 📚 References

- [NumPy Official Docs](https://numpy.org/doc/)
- [NumPy Cheat Sheet – DataCamp](https://www.datacamp.com/community/blog/python-numpy-cheat-sheet)

---

### ✍️ Notes

- Practice examples are based on Krishnaik's and DataCamp content.
- I will update this README as I progress to cover all industry-level NumPy concepts.

## What is NumPy and Why Use It?

NumPy (Numerical Python) is a Python library used for working with arrays. It is the foundation for almost all numerical and scientific computing in Python.

🔥 Why Use NumPy?
-> Much faster than native Python lists.
-> Supports multi-dimensional arrays.
-> Provides mathematical functions, random number generation, linear algebra, Fourier transforms, etc.
-> Backbone for Pandas, TensorFlow, Scikit-Learn, and more.

🧠 Python List vs NumPy Array

| Feature       | Python List   | NumPy Array                     |
| ------------- | ------------- | ------------------------------- |
| Data Type     | Can mix types | One type only (faster)          |
| Speed         | Slower        | Much faster (C backend)         |
| Functionality | Basic         | Advanced math, stats, reshaping |
| Memory        | Higher usage  | Lower and efficient             |
| Vectorization | ❌ No         | ✅ Yes                          |

🛠️ Array Creation Methods in NumPy

NumPy gives us several ways to create arrays easily and efficiently — from manual values to auto-filled ranges.

| Function   | Description     | Example              | Output                        |
| ---------- | --------------- | -------------------- | ----------------------------- |
| array()    | From list/tuple | np.array([1, 2])     | [1 2]                         |
| arange()   | Like range()    | np.arange(1, 5, 0.5) | [1. 1.5 2. 2.5 3. 3.5 4. 4.5] |
| zeros()    | Fill with 0s    | np.zeros((2, 2))     | [[0. 0.]                      |
|            |                 |                      | [0. 0.]]                      |
| ones()     | Fill with 1s    | np.ones((3, 1))      | [[1.]                         |
|            |                 |                      | [1.]                          |
|            |                 |                      | [1.]]                         |
| full()     | Fill with value | np.full((2, 3), 8)   | [[8 8 8]                      |
|            |                 |                      | [8 8 8]]                      |
| linspace() | Even spacing    | np.linspace(0, 1, 5) | [0. 0.25 0.5 0.75 1. ]        |

NumPy Data Types (dtype) & Type Conversion

NumPy arrays are faster than Python lists because they use fixed-size, homogeneous data types (All elements in a NumPy array must be of the same data type.).
This lets NumPy perform low-level optimizations in memory and speed.

## 🟡 Indexing, Slicing & Iteration in NumPy

Accessing, filtering, and navigating through NumPy arrays efficiently is essential for data manipulation and analysis. This section covers how to work with 1D, 2D, and 3D arrays using powerful indexing techniques.

### 📌 Indexing

You can access elements in any dimensional array using index positions.

| Array Type | Example        | Description                 |
| ---------- | -------------- | --------------------------- |
| 1D         | `arr[3]`       | 4th element                 |
| 2D         | `arr[1, 2]`    | Row 2, Column 3             |
| 3D         | `arr[0, 1, 1]` | 1st block, 2nd row, 2nd col |

Negative indices like `arr[-1]` are used to access elements from the end.

---

### 📌 Slicing

You can extract subarrays using slicing syntax: `start:stop:step`.

| Example        | Description                |
| -------------- | -------------------------- |
| `arr[1:4]`     | Elements from index 1 to 3 |
| `arr[::2]`     | Every second element       |
| `arr[1:3, :2]` | 2D: rows 1-2, columns 0-1  |
| `arr[-2::-3]`  | Reverse slicing with step  |

---

### 📌 Fancy Indexing

Fancy indexing lets you access multiple values using a list or array of indices.

```python
arr[[1, 3, 5]]
arr[arr % 2 == 0]
```

---

### 📌 Boolean Indexing (Conditional Selection)

You can filter values based on conditions and even modify them.

```python
arr[arr > 10]
arr[arr < 5] = 0
```

---

### 📌 Using `np.where()`

This function returns the indices where a condition holds true.

```python
np.where(arr > 50)
```

---

### 📌 Iterating Through Arrays

Loop through rows or use flat iteration:

```python
for row in arr_2d:
    print(row)

for value in np.nditer(arr_2d):
    print(value)
```

---

🧪 **Practical Insight**:  
These operations help filter top scores in a dataset, select specific regions of an image, or extract useful data points from large arrays.

# 🔵 Array Operations & Broadcasting in NumPy

When working with data arrays in AI/ML (like user ratings, item features, preferences), **speed and efficiency** are critical — that's where **NumPy** shines.  
Think of every user or movie as a row of numbers (**arrays**) that describe them — we often need to:

- **Add two arrays** together (e.g., user preferences + item features)
- **Scale features** (e.g., normalize ratings)
- **Compute similarities** (e.g., dot products, differences)
- **Summarize statistics** (e.g., average, total, variance)

---

## ✅ Element-wise Operations

Basic math operations applied directly to arrays of the same shape.

```python
import numpy as np

arr1 = np.array([10, 20, 30])
arr2 = np.array([40, 50, 60])

print(arr1 + arr2)  # [50 70 90]
print(arr1 * arr2)  # [400 1000 1800]
print(arr1 - arr2)  # [-30 -30 -30]
print(arr1 / arr2)  # [0.25 0.4  0.5]
print(arr1 ** arr2) # Exponentiation
```

---

## ✅ Broadcasting

**Broadcasting** allows operations between arrays of different shapes without copying data, stretching the smaller array efficiently.

```python
print(arr1 + 3)  # Scalar added to every element

matrix = np.array([[1, 2, 3], [4, 5, 6]])
new_row = np.array([7, 8, 9])
print(matrix + new_row)  # Broadcasting row-wise
```

---

## ✅ Aggregation Functions

Summarize arrays with important statistics.

```python
data = np.array([[80, 85, 90],
                 [70, 75, 80],
                 [90, 95, 100]])

print(np.sum(data))      # Total sum
print(np.mean(data))     # Average
print(np.std(data))      # Standard deviation
print(np.var(data))      # Variance

print(np.sum(data, axis=0))  # Sum column-wise
print(np.sum(data, axis=1))  # Sum row-wise
```

---

## ✅ Sorting, Searching, Counting

```python
arr = np.array([10, 5, 8, 12])

print(np.sort(arr))           # Sort the array
print(np.argmax(arr))         # Index of maximum value
print(np.argmin(arr))         # Index of minimum value
print(np.count_nonzero(arr>8))# Count values greater than 8
```

---

# 🔴 Reshaping & Manipulation in NumPy

Working with datasets (especially images) often requires reshaping arrays for modeling and visualization.

## 🎯 Real-World Scenario

Images are 3D arrays (height, width, channels), but ML models may expect 2D input (samples, features).  
You must **reshape, flatten, and transpose** arrays efficiently!

---

## ✅ Reshaping Arrays

```python
a = np.array([1,2,3,4,5,6,7,8,9,10])
print(a.reshape(2,5))  # Reshape to 2 rows, 5 columns
```

---

## ✅ Flatten vs Ravel

```python
b = np.array([[1,2,3],[4,5,6]])

print(b.flatten())  # Always returns a **copy**
print(b.ravel())    # Returns a **view** (faster, memory efficient)
```

---

## ✅ Transposing Arrays

```python
c = np.array([[11,12,13], [14,15,16]])

print(c.transpose())
print(c.T)  # Same result as transpose()
```

---

## ✅ Concatenation and Stacking

```python
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print(np.concatenate((a,b), axis=1))  # Horizontal concat
print(np.stack((a,b)))                # Stack along new axis
print(np.vstack((a,b)))               # Vertical stacking
print(np.hstack((a,b)))               # Horizontal stacking
```

---

## ✅ Splitting Arrays

```python
arr = np.array([10,20,30,40,50,60])

print(np.split(arr, 3))  # Split into 3 equal parts
```

---

# 🧪 Practice Tasks (Completed)

✅ Create 1D array and reshape to 2D.  
✅ Flatten 2D array back to 1D.  
✅ Transpose a 2D array.  
✅ Stack arrays vertically and horizontally.  
✅ Split 1D array into multiple parts.

---

# 📚 Notes

- Examples and exercises are based on Krishnaik’s and DataCamp’s NumPy content.
- Concepts are learned through small real-world use-cases to build strong intuition.



# 📘 Day 5: Mathematical Functions in NumPy

## ✈️ Real-World Scenario

Suppose you're building a machine learning model to predict **flight delays**.  
You need to **normalize features** using math functions like logarithms,  
or adjust **sensor data** using **trigonometric transformations** for better prediction.

NumPy provides **powerful mathematical functions** to handle these operations **efficiently**.

---

## 🔢 Topics Covered

### ➡️ 1. Trigonometric Functions

You can apply functions like `sin()`, `cos()`, and `tan()` on arrays — useful in fields like physics, engineering, and data normalization.

```python
import numpy as np

angles = np.array([0, np.pi/2, np.pi])

print(np.sin(angles))  # [ 0.  1.  0.]
print(np.cos(angles))  # [ 1.  0. -1.]
```

- `np.pi` represents π (Pi value).
- **Angles must be given in radians** for NumPy trig functions.

---

### ➡️ 2. Exponential and Logarithmic Functions

Used widely in machine learning, finance, and data transformations.

```python
import numpy as np

values = np.array([1, 2, 3])

print(np.exp(values))    # e^x for each element
print(np.log(values))    # Natural log (base e)
print(np.log10(values))  # Log base 10
```

- `np.exp()` is useful when modeling **exponential growth**.
- `np.log()` and `np.log10()` are important for **feature scaling** and **transformations**.

---

### ➡️ 3. Rounding Functions

Adjust floating-point numbers for reporting, decision-making, or data cleaning.

```python
import numpy as np

nums = np.array([1.2, 2.5, 3.7])

print(np.floor(nums))  # Rounds **down** to nearest integer
print(np.ceil(nums))   # Rounds **up** to nearest integer
print(np.round(nums))  # Rounds to nearest integer
```

- `floor()` always rounds **down**.
- `ceil()` always rounds **up**.
- `round()` rounds to the **nearest integer** based on decimal value.

---

