print(">>> main.py loaded")
from fastapi import FastAPI, UploadFile, File
from app.utils import preprocess_image
from app.predict import predict_image
import traceback

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Plant Disease Prediction API"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        print("Request received")

        image = preprocess_image(file.file)
        print("Image preprocessed")

        disease, confidence = predict_image(image)
        print("Prediction completed")

        return {
            "disease": disease,
            "confidence": round(confidence, 2)
        }

    except Exception as e:
        traceback.print_exc()   # This prints the FULL error in the terminal
        return {"error": str(e)}