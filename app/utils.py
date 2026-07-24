from PIL import Image
import numpy as np
from tensorflow.keras.applications.efficientnet import preprocess_input

def preprocess_image(file):
    image = Image.open(file).convert("RGB")
    image = image.resize((224, 224))

    image = np.array(image, dtype=np.float32)
    image = preprocess_input(image)
    image = np.expand_dims(image, axis=0)

    return image

