# Plant Disease Classification Using Deep Learning

## Overview

This project is a deep learning-based plant disease classification system developed using TensorFlow and MobileNetV2. The model classifies plant leaf images into 15 different disease categories and healthy classes from the PlantVillage dataset.

A Streamlit web application is provided to upload leaf images and obtain disease predictions with confidence scores.

---

## Features

* Plant leaf disease classification
* 15 disease and healthy classes
* Transfer learning using MobileNetV2
* Image upload interface using Streamlit
* Real-time prediction
* Confidence score display
* User-friendly web application

---

## Dataset

Dataset: PlantVillage

Total Images: 20,638

Number of Classes: 15

Classes:

* Pepper__bell___Bacterial_spot
* Pepper__bell___healthy
* Potato___Early_blight
* Potato___Late_blight
* Potato___healthy
* Tomato_Bacterial_spot
* Tomato_Early_blight
* Tomato_Late_blight
* Tomato_Leaf_Mold
* Tomato_Septoria_leaf_spot
* Tomato_Spider_mites_Two_spotted_spider_mite
* Tomato__Target_Spot
* Tomato__Tomato_YellowLeaf__Curl_Virus
* Tomato__Tomato_mosaic_virus
* Tomato_healthy

---

## Technologies Used

* Python
* TensorFlow
* MobileNetV2
* NumPy
* Pillow
* Streamlit

---

## Model Performance

* Training Accuracy: 92.4%
* Validation Accuracy: 91.8%

---

## Project Structure

Plant_Disease_Predictor/

├── app.py

├── classes.py

├── plant_disease_model.keras

├── requirements.txt

└── README.md

---

## Installation

Install required packages:

pip install -r requirements.txt

---

## Run Application

Start Streamlit:

streamlit run app.py

or

py -m streamlit run app.py

---

## Application Workflow

1. Upload a plant leaf image.
2. Preprocess image.
3. Predict disease using trained model.
4. Display disease name.
5. Display prediction confidence.

---

## Future Enhancements

* Disease treatment recommendations
* Fertilizer suggestions
* Mobile application deployment
* Multi-language support
* Cloud deployment

---

## Author

Praveena Gajula

Plant Disease Classification Project
