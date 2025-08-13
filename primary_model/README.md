# Retinal Disease Classification Using CNN and Transfer Learning

This project classifies OCT (Optical Coherence Tomography) images into **CNV**, **DME**, **Drusen**, and **Normal** using CNNs and transfer learning. The final model was **ResNet-18**, chosen for its balance of accuracy, efficiency, and reduced overfitting risk compared to deeper networks.

## Model & Training
- **Architecture:** ResNet-18 (18 layers, 11.6M parameters) with residual connections; final layer modified for 4-class output  
- **Input:** 224×224 RGB OCT images  
- **Split:** 70% train / 15% validation / 15% test  
- **Hyperparameters:** Batch size = 256, Learning rate = 0.002, Epochs = 5, Optimizer = Adam  

## Dataset
- **Small dataset:** 50 images/class (200 total) for initial testing  
- **Large dataset:** 3,000 images/class (12,000 total) for final evaluation; no overlap with small dataset  

## Results
ResNet-18 achieved the highest accuracy among tested models:

| Model     | Train (%) | Val (%) | Test (%) |
|-----------|-----------|---------|----------|
| **ResNet-18** | **97.08**  | **92.72** | **91.28** |
| VGG-11    | 91.87     | 82.33   | 80.39    |
| AlexNet   | 84.25     | 80.67   | 78.78    |
| VGG-16    | 86.64     | 77.61   | 78.11    |
| ResNet-50 | 73.13     | 72.11   | 72.00    |

ResNet-18 outperformed deeper models, offering the best accuracy with lower computational cost.

