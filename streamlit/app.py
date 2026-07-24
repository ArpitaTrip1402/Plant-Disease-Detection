import streamlit as st
import requests

st.set_page_config(page_title="Plant Disease Detection", page_icon="🌿")

st.title("🌿 Plant Disease Detection")
st.write("Upload a leaf image to predict the disease.")

uploaded_file = st.file_uploader(
    "Choose a leaf image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    if st.button("Predict"):

        files = {"file": uploaded_file.getvalue()}

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            files=files
        )

        if response.status_code == 200:

            result = response.json()

            st.success("Prediction Completed!")

            st.write(f"### Disease: {result['disease']}")
            st.write(f"### Confidence: {result['confidence']} %")

        else:
            st.error("Prediction Failed!")