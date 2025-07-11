import os

base_dir = "/Users/yoishikrakshit/Downloads/CellData/OCT_split"
splits = ["train", "val", "test"]
classes = ["CNV", "DME", "DRUSEN", "NORMAL"]

for split in splits:
    print(f"\n{split.upper()} set counts:")
    for cls in classes:
        path = os.path.join(base_dir, split, cls)
        count = len([f for f in os.listdir(path) if not f.startswith('.')])
        print(f"  {cls}: {count} images")
