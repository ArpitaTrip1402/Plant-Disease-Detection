print(">>> predict.py loaded")
import numpy as np
import pickle
from tensorflow.keras.models import load_model

model = load_model("model/Plant_disease_model.keras")

with open("model/class_names.pkl", "rb") as f:
    class_names = pickle.load(f)

def predict_image(img):
    print("Input shape:", img.shape)
    print("Input dtype:", img.dtype)
    print("Min:", img.min())
    print("Max:", img.max())

    prediction = model.predict(img, verbose=0)

    top5 = np.argsort(prediction[0])[-5:][::-1]

    print("\nTop 5 Predictions")
    for i in top5:
     print(f"{class_names[i]} : {prediction[0][i]*100:.2f}%")

    print("Prediction shape:", prediction.shape)
    print("Prediction:", prediction)

    index = np.argmax(prediction)
    disease = class_names[index]

    print("Predicted index:", index)
    print("Predicted class:", disease)

    confidence = float(np.max(prediction)) * 100


    return disease, confidence
