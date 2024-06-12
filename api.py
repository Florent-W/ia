from fastapi import FastAPI, File, UploadFile, HTTPException
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

    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Le fichier doit être un fichier CSV.")
    
    df = pd.read_csv(io.StringIO(content.decode('utf-8')))

    if 'home_team' not in df.columns or 'away_team' not in df.columns or 'home_win' not in df.columns:
        raise HTTPException(status_code=400, detail="Les colonnes 'home_team', 'away_team' et 'home_win' sont requises.")
    
    response = train(df)
    return {"score": response}

@app.post("/predict")
async def predict_match(teams: dict):
    if 'team1' not in teams or 'team2' not in teams:
        raise HTTPException(status_code=400, detail="Les noms des équipes 'team1' et 'team2' sont requis.")
    response = predict(teams)
    return response

@app.get("/model")
async def get_model(text: str):
    if not text:
        raise HTTPException(status_code=400, detail="Le texte est requis.")
    response = callOpenAI(text)
    return {"response": response}