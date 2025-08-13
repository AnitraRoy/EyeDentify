# Retinal Disease Classification Using SVM and Deep Features

This project implements a **Support Vector Machine (SVM)** classifier with **Radial Basis Function (RBF) kernel** to classify **OCT (Optical Coherence Tomography)** scans into four categories: **CNV (Choroidal Neovascularization), DME (Diabetic Macular Edema), Drusen, and Normal**. The model combines both deep features and handcrafted features for robust feature extraction and classification.

## Project Overview

The baseline model is an **SVM classifier** trained to classify OCT scans into four categories. The feature extraction combines:

1. **Deep Features**: Extracted from a pre-trained **ResNet-152** model, capturing global image representations from large-scale natural image data.
2. **Handcrafted Features**: Derived using **Local Binary Pattern (LBP)** for texture analysis and **Sobel filters** for edge detection, focusing on local patterns and structural changes in retinal images.

The SVM classifier is trained with a **Radial Basis Function (RBF) kernel** after feature scaling, **Principal Component Analysis (PCA)** for dimensionality reduction, and cross-validation.


## Model & Training
- **Pre-Trained by:** ResNet-152
- **Input:** 224×224 RGB OCT images  
- **Split:** 70% train / 15% validation / 15% test  
- **Hyperparameters:** PCA = 20, regularization strength (C) = 10, kernel coefficient (γ) = default

Note: these optimal hyperparameters were found through GridSearchCV

## Dataset
- **Small dataset:** 50 images/class (200 total) for initial testing  
- **Large dataset:** 3,000 images/class (12,000 total) for final evaluation; no overlap with small dataset  
- **New dataset:** From the Retinal OCT Image Classification C8 dataset on Kaggle, containing a different distribution from the UCSD dataset. A balanced 50 images/class (200 total) was sampled, and models were tested using the same UCSD-trained hyperparameters without further tuning.  

## Results

The baseline performed well on the small dataset, but poor on the large dataset, and even poorer on the new dataset:

| Dataset     | Accuracy (%) |
|-------------|--------------|
| **Small**   | 78.33        |
| **Large**   | 54.36        |
| **New**     | 21.67        |

These results suggest that traditional machine learning models may not be well-suited for retinal disease classification across diverse datasets.
