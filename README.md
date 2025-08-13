# EyeDentify
EyeDentify is a deep learning-based project designed to automate the classification of retinal diseases using **Optical Coherence Tomography (OCT)** images. The primary goal of this project is to improve diagnostic efficiency and accuracy for retinal conditions, specifically **Choroidal Neovascularization (CNV)**, **Drusen**, **Diabetic Macular Edema (DME)**, and **Normal** retinal health.

## Overview

OCT images are widely used in ophthalmology to capture detailed images of the retina's layers, assisting in the diagnosis of retinal diseases. However, manual interpretation of these images can be time-consuming and prone to errors. EyeDentify utilizes **ResNet-18**, a deep learning model based on **Convolutional Neural Networks (CNNs)**, to automatically classify these images into different categories, thereby enabling quicker and more accurate diagnoses.

## Key Features
- **Deep Learning-based Classification**: Utilizes the **ResNet-18 CNN** to automatically classify OCT images.
- **Four Classification Categories**: CNV, Drusen, DME, and Normal retinal health.
- **High Performance**: Achieved a test accuracy of 91.28%, with an **AUC of 0.99**, indicating near-perfect model performance.
- **Comparative Evaluation**: Benchmarked against a traditional **Support Vector Machine (SVM)** classifier for classification.

## Objectives
- **Increase Diagnostic Efficiency**: Speed up retinal disease diagnosis by automating the process using deep learning models.
- **Improve Accuracy**: Ensure more reliable classification of OCT images, reducing human error and variability.
- **Clinical Application**: Make the model scalable for real-world use in clinical settings, ensuring faster detection and intervention for patients.
