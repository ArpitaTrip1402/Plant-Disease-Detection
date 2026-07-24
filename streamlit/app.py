import streamlit as st
import requests
from PIL import Image

# -------------------------
# CONFIG
# -------------------------
API_URL = "https://plant-disease-detection-y1cg.onrender.com/predict"

st.set_page_config(
    page_title="Plant Disease Detection",
    page_icon="🌿",
    layout="centered"
)

st.title("🌿 Plant Disease Detection")
st.write("Upload a leaf image and detect its disease using AI.")

uploaded_file = st.file_uploader(
    "Choose a leaf image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Predict Disease"):

        with st.spinner("Predicting..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type,
                )
            }

            try:

                response = requests.post(API_URL, files=files)

                if response.status_code == 200:

                    result = response.json()

                    st.success("Prediction Completed!")

                    st.subheader("Disease")

                    st.write(result["disease"])

                    st.subheader("Confidence")

                    st.write(f"{result['confidence']:.2f}%")

                else:

                    st.error(f"API Error: {response.text}")

            except Exception as e:

                st.error(str(e))