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

5. **Stratified Splitting**
   - Splits resized images into `train`, `val`, and `test` sets (70/15/15).
   - Ensures each class is proportionally represented.
   - Saves results in `OCT_split/`.

6. **Verification of Split Counts**
   - Displays per-class image counts in each split.
   - Ensures the stratified split maintains the expected distribution.

7. **Merge by Class**
   - Combines images from multiple sources into unified class directories.
   - Useful for aggregating datasets before running earlier preprocessing steps.

---

## Scripts

| Script Name                   | Description |
|------------------------------|-------------|
| `1clean_and_prepare_oct.py`  | Scans raw folders and deletes any corrupted or unreadable files. |
| `2check_labels.py`           | Checks that the dataset folder structure and labels are correct. |
| `3resize_and_normalize_oct.py`| Resizes and normalizes all images. Creates `OCT_resized/`. |
| `4check_image_size.py`       | Displays resolution and pixel statistics for sample images. |
| `5split_stratified_oct.py`   | Performs train/val/test stratified split. Creates `OCT_split/`. |
| `6verify_split_counts.py`    | Prints number of images per class in each split. |
| `7merge_by_class.py`         | Merges images from multiple datasets into unified class folders. |

## Notes

- Run each script from the project root with:
  ```bash
  python3 data_processing/script_name.py
