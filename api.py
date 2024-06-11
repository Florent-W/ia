from fastapi import FastAPI
from tensorflow.keras.models import load_model

from pydantic import BaseModel

app = FastAPI(
    title="L'API The Predictor",
    description="L'API va permettre de faire des prédictions sur les rencontres de matchs internationaux de football.",
)

@app.post("/predict", tags=["Numbers"])
def predict(data:Data):
    print(True)
    model = load_model('model.h5')