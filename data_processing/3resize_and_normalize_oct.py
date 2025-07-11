import os
from PIL import Image
import numpy as np

# === CONFIG ===
input_base = "/Users/yoishikrakshit/Downloads/CellData/OCT"
output_base = "/Users/yoishikrakshit/Downloads/CellData/OCT_resized"
target_size = (224, 224)

def resize_and_normalize_images(subset):
    input_path = os.path.join(input_base, subset)
    output_path = os.path.join(output_base, subset)
    os.makedirs(output_path, exist_ok=True)

    for label in os.listdir(input_path):
        if label.startswith('.'):  # skip .DS_Store or hidden files
            continue
        input_class_path = os.path.join(input_path, label)
        output_class_path = os.path.join(output_path, label)
        os.makedirs(output_class_path, exist_ok=True)

        for filename in os.listdir(input_class_path):
            if filename.startswith('.'):
                continue
            input_img_path = os.path.join(input_class_path, filename)
            output_img_path = os.path.join(output_class_path, filename)

            try:
                img = Image.open(input_img_path).convert("L")  # grayscale
                img = img.resize(target_size, Image.BILINEAR)
                img_array = np.array(img) / 255.0
                normalized_img = Image.fromarray((img_array * 255).astype(np.uint8))
                normalized_img.save(output_img_path)
            except Exception as e:
                print(f"Error processing {input_img_path}: {e}")

    print(f"Finished processing {subset} set.")

# === RUN FOR BOTH TRAIN AND TEST ===
if __name__ == "__main__":
    resize_and_normalize_images("train")
    resize_and_normalize_images("test")
