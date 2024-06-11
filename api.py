from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from function import train, predict, callOpenAI
import pandas as pd
import io

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/training")
async def create_training(file: UploadFile = File(...)):
    content = await file.read()
    df = pd.read_csv(io.StringIO(content.decode('utf-8')))
    response = train(df)
    return {"score": response}

@app.post("/predict")
async def predict_match(teams: dict):
    response = predict(teams)
    return response

@app.get("/model")
async def get_model():
    response = callOpenAI("Qui est le meilleur joueur de football ?")
    return response