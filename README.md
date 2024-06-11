# ia

## Installation

```bash
pip install -r requirements.txt
```

## Lancer le serveur

```bash
fastapi dev api.py
```

## Endpoints

- `POST /training` - Entrainer le modèle avec un fichier CSV (data.csv)

  ```json
  // form-data
  {
    "file": "<data.csv>"
  }
  ```

- `POST /predict` - Prédire l'équipe gagnante d'un match

  ```json
  {
    "team1": "France",
    "team2": "Germany"
  }
  ```

- `GET /model` - Appeler le modèle GPT-3

## Équipe

- Florent Weltmann
- Dantin Durand
- Bryan Kwuimo Kwekam
