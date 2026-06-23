import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

from classes import class_names

model = tf.keras.models.load_model("plant_disease_model.keras")

st.set_page_config(
    page_title="Plant Disease Detection",
    page_icon="🌿"
)

st.title("🌿 Plant Disease Classification")

uploaded_file = st.file_uploader(
    "Choose a leaf image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    if st.button("Predict"):

        img = image.resize((224,224))

        img_array = np.array(img)

        if len(img_array.shape) == 2:
            img_array = np.stack((img_array,) * 3, axis=-1)

        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(
            img_array,
            verbose=0
        )

        predicted_class = class_names[
            np.argmax(prediction)
        ]

        confidence = np.max(prediction) * 100

        st.success(
            f"Prediction: {predicted_class}"
        )

        st.info(
            f"Confidence: {confidence:.2f}%"
        )