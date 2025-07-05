# Data Processing Scripts

This folder contains all scripts used to prepare the OCT dataset for model training.

## Workflow Summary

1. **Cleaning**
   - Removes corrupted or unreadable image files from each class directory.

2. **Resizing & Normalizing**
   - Converts images to grayscale.
   - Resizes to 224×224 pixels.
   - Normalizes pixel values to [0, 1].
   - Saves processed images into `OCT_resized/`.

3. **Stratified Splitting**
   - Splits resized images into `train`, `val`, and `test` sets (70/15/15).
   - Ensures each class is proportionally represented.
   - Saves results in `OCT_split/`.

4. **Verification**
   - Confirms that images are correctly sized and normalized.
   - Displays per-class image counts in each split set.

---

## Scripts

| Script Name                   | Description |
|------------------------------|-------------|
| `clean_and_prepare_oct.py`   | Scans raw folders and deletes any corrupted or unreadable files. |
| `resize_and_normalize_oct.py`| Resizes and normalizes all images. Creates `OCT_resized/`. |
| `split_stratified_oct.py`    | Performs train/val/test stratified split. Creates `OCT_split/`. |
| `verify_split_counts.py`     | Prints number of images per class in each split. |
| `check_labels.py`            | Optional check for expected folder structure (CNV, DME, etc.). |
| `check_image_size.py`        | Displays the resolution and pixel stats of a sample image. |

---

## Notes

- Run each script from the project root with:
  ```bash
  python3 data_processing/script_name.py
