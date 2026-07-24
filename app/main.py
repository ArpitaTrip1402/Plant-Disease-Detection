from fastapi import FastAPI, UploadFile, File, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.utils import preprocess_image
from app.predict import predict_image


app = FastAPI()

# Templates
templates = Jinja2Templates(directory="app/templates")

# Static folder
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# Home Page
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )

# Prediction API
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = preprocess_image(file.file)

    disease, confidence = predict_image(image)

    return {
        "disease": disease,
        "confidence": round(confidence, 2)
    }