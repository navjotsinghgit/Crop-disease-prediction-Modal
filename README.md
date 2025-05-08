# 🌿 Crop Disease Prediction using CNN | Deep Learning in Agriculture

This project is a deep learning-based solution for **predicting diseases in crop leaves** using a Convolutional Neural Network (CNN). Trained on a dataset of **55,000+ images** of commonly cultivated plants, the model detects diseases with over **90% accuracy**, helping farmers and agri-tech systems take early preventive actions.

## 🧠 Model Overview

- 🔍 **Architecture**: 5-layer Convolutional Neural Network
- 🧾 **Dataset**: ~55,000 labeled leaf images from various crop species
- 39 Classes
  61486 Train images
  17676 Test images
- ⏱️ **Training**: 10 epochs
- 🎯 **Accuracy**: >90% on validation set

## 🏷️ Classes Covered

Includes a variety of crops and their most common diseases. Examples:
- Tomato (e.g., Early Blight, Late Blight)
- Corn (e.g., Leaf Spot, Common Rust)
- Potato, Grape, Apple, etc.

> The dataset was preprocessed with resizing, normalization, and augmentation for better generalization.

## 🛠️ Tech Stack

- 🐍 Python 3.x
- 🧠 TensorFlow / Keras
- 🖼️ OpenCV (for image pre-processing)
- 📊 Matplotlib (for plotting results)
- ⚙️ NumPy
- Django
- the architecture of the directory is in the following format-
- crop_detection_app/
├── crop_model/            # Django app for ML model
│   ├── views.py           # Handles HTML and API logic
│   ├── urls.py            # Route config
│   └── templates/         # HTML templates
│       └── index.html     # UI for predictions
├── crop_detection_app/    # Project settings
│   ├── settings.py        # Connect MySQL here
│   ├── urls.py
├── manage.py
├── Model.hdf5             # Your trained model
└── Crop.ipynb             # Notebook reference

