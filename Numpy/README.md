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

| File | Description |
|------|-------------|
| `array_basics.py` | Creating and exploring arrays |
| `slicing_examples.py` | Indexing and slicing arrays |
| `operations_demo.py` | Element-wise operations |
| `reshaping.py` | Reshape and array manipulation |
| `random_usage.py` | Using NumPy's random module |
| `performance_comparison.py` | NumPy vs Python lists |
| `notebook.ipynb` | Jupyter notebook for notes and practice |

## 📚 References

- [NumPy Official Docs](https://numpy.org/doc/)
- [NumPy Cheat Sheet – DataCamp](https://www.datacamp.com/community/blog/python-numpy-cheat-sheet)

---

### ✍️ Notes

- Practice examples are based on Krishnaik's and DataCamp content.
- I will update this README as I progress to cover all industry-level NumPy concepts.


## What is NumPy and Why Use It? ##
NumPy (Numerical Python) is a Python library used for working with arrays. It is the foundation for almost all numerical and scientific computing in Python.

🔥 Why Use NumPy?
    -> Much faster than native Python lists.
    -> Supports multi-dimensional arrays.
    -> Provides mathematical functions, random number generation, linear algebra, Fourier transforms, etc.
    -> Backbone for Pandas, TensorFlow, Scikit-Learn, and more.

🧠 Python List vs NumPy Array

| Feature         | Python List                | NumPy Array                     |
|----------------|----------------------------|----------------------------------|
| Data Type      | Can mix types              | One type only (faster)          |
| Speed          | Slower                     | Much faster (C backend)         |
| Functionality  | Basic                      | Advanced math, stats, reshaping |
| Memory         | Higher usage               | Lower and efficient             |
| Vectorization  | ❌ No                      | ✅ Yes                           |


🛠️ Array Creation Methods in NumPy

NumPy gives us several ways to create arrays easily and efficiently — from manual values to auto-filled ranges.

| Function   | Description        | Example                   | Output                        |
|------------|--------------------|---------------------------|-------------------------------|
| array()    | From list/tuple    | np.array([1, 2])          | [1 2]                         |
| arange()   | Like range()       | np.arange(1, 5, 0.5)      | [1.  1.5 2.  2.5 3.  3.5 4.  4.5] |
| zeros()    | Fill with 0s       | np.zeros((2, 2))          | [[0. 0.]                      |
|            |                    |                           |  [0. 0.]]                     |
| ones()     | Fill with 1s       | np.ones((3, 1))           | [[1.]                         |
|            |                    |                           |  [1.]                         |
|            |                    |                           |  [1.]]                        |
| full()     | Fill with value    | np.full((2, 3), 8)        | [[8 8 8]                      |
|            |                    |                           |  [8 8 8]]                     |
| linspace() | Even spacing       | np.linspace(0, 1, 5)      | [0.   0.25 0.5  0.75 1.  ]    |


NumPy Data Types (dtype) & Type Conversion

NumPy arrays are faster than Python lists because they use fixed-size, homogeneous data types (All elements in a NumPy array must be of the same data type.).
This lets NumPy perform low-level optimizations in memory and speed.

## 🟡 Indexing, Slicing & Iteration in NumPy

Accessing, filtering, and navigating through NumPy arrays efficiently is essential for data manipulation and analysis. This section covers how to work with 1D, 2D, and 3D arrays using powerful indexing techniques.

### 📌 Indexing

You can access elements in any dimensional array using index positions.

| Array Type | Example         | Description                   |
|------------|------------------|-------------------------------|
| 1D         | `arr[3]`         | 4th element                   |
| 2D         | `arr[1, 2]`      | Row 2, Column 3               |
| 3D         | `arr[0, 1, 1]`   | 1st block, 2nd row, 2nd col   |

Negative indices like `arr[-1]` are used to access elements from the end.

---

### 📌 Slicing

You can extract subarrays using slicing syntax: `start:stop:step`.

| Example            | Description                          |
|--------------------|--------------------------------------|
| `arr[1:4]`         | Elements from index 1 to 3           |
| `arr[::2]`         | Every second element                 |
| `arr[1:3, :2]`     | 2D: rows 1-2, columns 0-1            |
| `arr[-2::-3]`      | Reverse slicing with step            |

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
