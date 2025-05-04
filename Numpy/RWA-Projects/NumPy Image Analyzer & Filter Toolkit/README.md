# 📸 NumPy Image Analyzer & Filter Toolkit

A simple and powerful project that showcases how **NumPy** can be used to manipulate, analyze, and filter image data using real-world techniques like grayscale conversion, normalization, brightness, contrast, and more — all without deep image libraries.

---

## ✅ Features

- Convert images to grayscale
- Normalize image pixel values
- Adjust image brightness
- Enhance image contrast
- Save processed images automatically
- Modular project structure for clean, extendable code

---

## 🚀 Technologies Used

- **NumPy** — for all array and mathematical operations
- **Pillow (PIL)** — to load and save images as arrays

---

## 💡 Why Use Pillow?

[Pillow](https://python-pillow.org/) is a lightweight and easy-to-use image processing library that lets you:
- Load images in various formats (JPG, PNG, etc.)
- Convert them into NumPy arrays for manipulation
- Save arrays back into image files (JPEG, PNG)

```bash
pip install pillow

```
---

## 🗂️ Project Structure

numpy-image-toolkit/
│
├── main.py              # 🔁 Main script to apply all filters
├── filters.py           # 🎨 Contains filter functions (grayscale, normalize, etc.)
├── utils.py             # 🧰 Load/save image helpers using Pillow
├── input/               # 📥 Folder for input images (e.g. input/cat.jpg)
├── output/              # 📤 Folder for saving processed images


## 📄 File Explanations

### `main.py`
- Loads an image from the `input/` folder
- Applies all available filters (grayscale, normalize, brightness, contrast)
- Saves each result to the `output/` folder
- Use this as the **entry point** of the project

---

### `filters.py`
Contains all the image transformation functions using NumPy:

- `to_grayscale(image)`
  - Converts RGB to grayscale using weighted average  
    `(R=0.299, G=0.587, B=0.114)`

- `normalize(image)`
  - Scales pixel values from 0–255 to 0–1 for ML use

- `adjust_brightness(image, factor)`
  - Adds a constant brightness factor to each pixel

- `adjust_contrast(image, factor)`
  - Multiplies pixel difference from mean to enhance contrast

⚡ All functions use **NumPy vectorization**, not loops.

---

### `utils.py`
Helper functions for working with images using Pillow:

- `load_image(path)`
  - Opens and converts an image to RGB, then converts it to a NumPy array

- `save_image(np_array, path)`
  - Converts NumPy array back into a PIL image and saves it as a file
