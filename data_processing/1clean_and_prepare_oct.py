import os
from PIL import Image, UnidentifiedImageError

def verify_and_clean_images(base_path):
    print(f"\nChecking: {base_path}")
    corrupted_count = 0
    total_checked = 0

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if not file.lower().endswith(('.jpeg', '.jpg', '.png')):
                continue
            file_path = os.path.join(root, file)
            total_checked += 1
            try:
                with Image.open(file_path) as img:
                    img.load()
            except (UnidentifiedImageError, IOError, SyntaxError):
                print(f"[REMOVED] Corrupted: {file_path}")
                os.remove(file_path)
                corrupted_count += 1

    print(f"Finished checking: {base_path}")
    print(f"Checked: {total_checked} files")
    print(f"Removed: {corrupted_count} corrupted files")

base_path = "/Users/yoishikrakshit/Downloads/CellData/OCT"

if __name__ == "__main__":
    verify_and_clean_images(os.path.join(base_path, "train"))
    verify_and_clean_images(os.path.join(base_path, "test"))
