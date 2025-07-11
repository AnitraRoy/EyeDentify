# Retinal Disease Classification Using SVM and Deep Features

This project implements a **Support Vector Machine (SVM)** classifier with **Radial Basis Function (RBF) kernel** to classify **OCT (Optical Coherence Tomography)** scans into four categories: **CNV (Choroidal Neovascularization), DME (Diabetic Macular Edema), Drusen, and Normal**. The model combines both deep features and handcrafted features for robust feature extraction and classification.

## Project Overview

The baseline model is an **SVM classifier** trained to classify OCT scans into four categories. The feature extraction combines:

1. **Deep Features**: Extracted from a pre-trained **ResNet-152** model, capturing global image representations from large-scale natural image data.
2. **Handcrafted Features**: Derived using **Local Binary Pattern (LBP)** for texture analysis and **Sobel filters** for edge detection, focusing on local patterns and structural changes in retinal images.

The SVM classifier is trained with a **Radial Basis Function (RBF) kernel** after feature scaling, **Principal Component Analysis (PCA)** for dimensionality reduction, and cross-validation.

## Results

The initial baseline model achieved an **accuracy of 68.33%**, with **macro-average precision**, **recall**, and **F1 scores** around 70%. After hyperparameter tuning using **grid search** and **cross-validation**, the model's accuracy improved to **78.33%**, and the **macro-average precision**, **recall**, and **F1 scores** increased to nearly 0.80. The model also showed improved performance in the **confusion matrix** and **ROC AUC scores**.