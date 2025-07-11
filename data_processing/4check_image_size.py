from PIL import Image
import os
import numpy as np

# === Use one of the actual folders — e.g., CNV in train ===
img_path = "/Users/yoishikrakshit/Downloads/CellData/OCT_resized/train/CNV"

print(f"Checking contents of: {img_path}")
print("Files found:", os.listdir(img_path))  # NEW LINE

# === Check if folder is empty ===
if len(os.listdir(img_path)) == 0:
    print("No images found in the folder!")
else:
    sample_file = os.listdir(img_path)[0]
    full_path = os.path.join(img_path, sample_file)

    with Image.open(full_path) as img:
        print("Size:", img.size)
        img_array = np.array(img)
        print("Min pixel value:", img_array.min())
        print("Max pixel value:", img_array.max())
