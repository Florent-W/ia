from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from function import train
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
    print("test")
    # Lire le contenu du fichier CSV
    content = await file.read()
    # Charger le CSV dans un DataFrame pandas
    df = pd.read_csv(io.StringIO(content.decode('utf-8')))
    # Appeler la fonction train avec le DataFrame
    response = train(df)
    # Retourner la réponse de la fonction train
    return {"response": response}