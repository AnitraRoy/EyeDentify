print("🚀 Script started")

import os
import shutil
import random
from sklearn.model_selection import train_test_split

# === CONFIGURATION ===
input_dir = "/Users/yoishikrakshit/Downloads/CellData/OCT_resized"
output_dir = "/Users/yoishikrakshit/Downloads/CellData/OCT_split"
classes = ["CNV", "DME", "DRUSEN", "NORMAL"]
split_ratio = [0.7, 0.15, 0.15]  # Train / Val / Test

def create_dirs(base):
    for split in ["train", "val", "test"]:
        for cls in classes:
            os.makedirs(os.path.join(base, split, cls), exist_ok=True)

def split_and_copy():
    create_dirs(output_dir)

    for cls in classes:
        print(f"Processing class: {cls}")
        images = []

        # Collect all images from resized train and test folders
        for split_folder in ["train", "test"]:
            full_path = os.path.join(input_dir, split_folder, cls)
            if not os.path.exists(full_path):
                continue
            for img_name in os.listdir(full_path):
                img_path = os.path.join(full_path, img_name)
                if img_name.startswith('.') or not os.path.isfile(img_path):
                    continue
                images.append(img_path)

        print(f"Found {len(images)} total {cls} images")

        # Stratified splitting
        train_imgs, temp_imgs = train_test_split(images, train_size=split_ratio[0], random_state=42)
        val_imgs, test_imgs = train_test_split(temp_imgs, test_size=0.5, random_state=42)

        # Copy files
        for img in train_imgs:
            shutil.copy(img, os.path.join(output_dir, "train", cls, os.path.basename(img)))
        for img in val_imgs:
            shutil.copy(img, os.path.join(output_dir, "val", cls, os.path.basename(img)))
        for img in test_imgs:
            shutil.copy(img, os.path.join(output_dir, "test", cls, os.path.basename(img)))

        print(f"{cls}: Train={len(train_imgs)}  Val={len(val_imgs)}  Test={len(test_imgs)}")

if __name__ == "__main__":
    split_and_copy()
print("Finished splitting and copying images.")