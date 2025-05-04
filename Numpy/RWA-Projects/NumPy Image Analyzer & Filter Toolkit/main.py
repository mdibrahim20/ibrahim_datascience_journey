from utils import load_image, save_image
from filters import to_grayscale,normalize,adjust_brightness,adjust_contrast
import os

input_path = "H:\\ibrahim_datascience_journey\\Numpy\\RWA-Projects\\NumPy Image Analyzer & Filter Toolkit\\input\\cat.jpg"
output_dir = "H:\\ibrahim_datascience_journey\\Numpy\\RWA-Projects\\NumPy Image Analyzer & Filter Toolkit\\output\\"

base_name = os.path.splitext(os.path.basename(input_path))[0]
print("Current Working Directory:", os.getcwd())
if not os.path.exists(input_path):
    print("❌ File not found at:", input_path)
else:
    print("✅ Found image at:", input_path)
    img = load_image(input_path)
    # Apply grayscale
    gray = to_grayscale(img)
    save_image(gray,os.path.join(output_dir,f"{base_name}_grayscale.jpg"))
    # Apply normalization
    norm = normalize(img) * 255
    save_image(norm,os.path.join(output_dir,f"{base_name}_normalized.jpg"))
    # Adjust Brightness
    bright = adjust_brightness(img,50)
    save_image(bright,os.path.join(output_dir,f"{base_name}_bright.jpg"))
    # Adjust Contrast
    contrast = adjust_contrast(img, 1.5)
    save_image(contrast, os.path.join(output_dir, f"{base_name}_contrast.jpg"))

    print("All filters applied and saved to output directory")