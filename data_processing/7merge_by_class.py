import os
import shutil
import random

# Settings
base_dir = "../OCT_split"
output_dir = "../OCT_by_class"
splits = ['train', 'val', 'test']
classes = ['CNV', 'DME', 'DRUSEN', 'NORMAL']
sample_size = 3000  # images per class

# Make output dir
os.makedirs(output_dir, exist_ok=True)

for cls in classes:
    dest_folder = os.path.join(output_dir, cls)
    os.makedirs(dest_folder, exist_ok=True)

    print(f"\nProcessing class: {cls}")

    all_images = []

    for split in splits:
        src_dir = os.path.join(base_dir, split, cls)
        if not os.path.exists(src_dir):
            print(f"  Missing: {src_dir}")
            continue

        for fname in os.listdir(src_dir):
            full_path = os.path.join(src_dir, fname)
            if os.path.isfile(full_path):
                all_images.append((full_path, f"{split}_{fname}"))

    print(f"  Found {len(all_images)} images total")

    # Shuffle and sample 3000
    random.shuffle(all_images)
    selected = all_images[:sample_size]

    for src, renamed in selected:
        dst = os.path.join(dest_folder, renamed)
        shutil.copy2(src, dst)

    print(f"  Copied {len(selected)} images → {dest_folder}")
