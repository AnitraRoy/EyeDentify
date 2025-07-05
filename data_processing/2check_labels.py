import os

# Set the path to your OCT dataset
base_path = "/Users/yoishikrakshit/Downloads/CellData/OCT"

# Loop through train and test folders
for subset in ["train", "test"]:
    folder_path = os.path.join(base_path, subset)
    if not os.path.exists(folder_path):
        print(f"❌ Folder not found: {folder_path}")
        continue

    print(f"\n📁 {subset.upper()} subfolders:")
    try:
        class_folders = sorted(os.listdir(folder_path))
        for cls in class_folders:
            full_path = os.path.join(folder_path, cls)
            if os.path.isdir(full_path):
                print(f"  - {cls}")
    except Exception as e:
        print(f"⚠️ Error reading {folder_path}: {e}")
