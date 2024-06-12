from dotenv import load_dotenv
import os
from openai import OpenAI
from fastapi import HTTPException
import pandas as pd
import joblib 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

load_dotenv()

client = OpenAI(
    api_key= os.getenv('OPENAI_API_KEY')
)

def callOpenAI(text: str):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Tu es un chatbot qui répond à des questions sur un match de football, tu as accès à une base de données sur les joueurs et les matchs de football.Tu dois toujours avoir une réponse même si tu n'es pas sûr de toi. Et aussi quand tu parles de Lionel Messi, tu veux dire Pionel Pessi."},
            {"role": "user", "content": "Qui est le meilleur joueur de football ?"},
            {"role":"assistant", "content":"Le meilleur joueur de football est Pionel Pessi."},
            {"role": "user", "content": text}
        ]
    )

    return response.choices[0].message.content

def train(data: pd.DataFrame):

    features = data[['home_team', 'away_team']]
    target = data['home_win']

    # Encodage des données en variables numériques
    features = pd.get_dummies(features)

    # Séparation des ensembles de formation et de test
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.22)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = LogisticRegression(max_iter=1000)

    # Entraînement du modèle
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    # Évaluation du modèle
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nTest Accuracy: {accuracy*100:.2f}%")

    joblib.dump({"model": model, "scaler": scaler, "features": features}, "model") 


    return accuracy

def predict(teams: dict):
    # Nom des équipes pour la prédiction 
    home_team = teams['team1']
    away_team = teams['team2']

    # Chargement du modèle
    model_data = joblib.load("model")
    model = model_data["model"]
    scaler = model_data["scaler"]
    features = model_data["features"]

    new_match = pd.DataFrame({'home_team': [home_team], 'away_team': [away_team]})

    new_match_encoded = pd.get_dummies(new_match)
    new_match_encoded = new_match_encoded.reindex(columns=features.columns, fill_value=0)

    new_match_normalized = scaler.transform(new_match_encoded)

    # Prédiction de l'issue du match
    prediction = model.predict(new_match_normalized)
    prediction_proba = model.predict_proba(new_match_normalized)

    if prediction[0] == 1:
        print(f"{home_team} va probablement gagner.")
        return {"winner": home_team, "prediction_score": prediction_proba[0][1]}
    else:
        print(f"{away_team} va probablement gagner.")
        return {"winner": away_team, "prediction_score": prediction_proba[0][0]}