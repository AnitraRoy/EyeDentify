# Retinal Disease Classification Using CNN and Transfer Learning

This project implements a **Convolutional Neural Network (CNN)** architecture to classify **OCT (Optical Coherence Tomography)** images into four classes: **CNV (Choroidal Neovascularization)**, **DME (Diabetic Macular Edema)**, **Drusen**, and **Normal**. The model was initially developed as a custom CNN, then extended using **transfer learning** with **ResNet-18** and **ResNet-50**. All models were trained using the **Adam optimizer** to take advantage of its adaptive learning rate and improved training efficiency compared to SGD.

## Project Overview

The initial model was a **custom CNN** consisting of two convolutional layers, two fully connected layers, and **ReLU activation functions**. However, due to its limited depth and number of trainable parameters, the model struggled to learn higher-level representations from the OCT data, resulting in lower classification performance.

To improve accuracy and generalization, the team applied **transfer learning** using **ResNet** models. Three configurations were trained with different hyperparameters, including:

1. **ResNet-18**: Shallow architecture with better performance on smaller datasets.
2. **ResNet-50**: Deeper architecture offering richer feature extraction but at the cost of overfitting risk and longer training time.

Key aspects of the training process included:
- **Batch size** = 16
- **Learning rate** = 0.001
- **Epochs** = 15
- **Early layers frozen** for ResNet-50 to reduce overfitting and lower computational cost

The dataset was initially composed of **1000 images per class**, but due to **hardware limitations on Google Colab** (e.g., high RAM and GPU usage), the team created a **smaller debug dataset** with **50 images per class** for faster experimentation and model tuning.

## Results

Among the models tested, **ResNet-18** achieved the best performance with:
- **Training accuracy**: 100%
- **Validation accuracy**: 80%
- **Test accuracy**: 96.7%

The training loss **steadily decreased across epochs**, indicating that the model was learning effectively. The **confusion matrix** revealed only a single misclassification (a DME scan labeled as Normal), and the **ROC curve** showed an **AUC of 1.00** across all four classes, indicating perfect class separation.

