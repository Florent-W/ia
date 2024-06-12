import streamlit as st


st.title("Documentation")

st.write("## 📝 Introduction")

st.write("Ce projet a pour but de prédire le résultat d'un match de football en fonction des équipes qui s'affrontent. Pour cela, nous avons utilisé un modèle de Logistic Regression entraîné sur un jeu de données contenant des informations sur des matchs de football passés.")

st.write("## 🚀 Installation")

st.write("Pour installer les dépendances du projet, vous pouvez exécuter la commande suivante :")
st.code("pip install -r requirements.txt")

st.write("## 📚 Utilisation")
st.code("uvicorn api:app --reload")
st.code("streamlit run app.py")

st.write("## 📡 Endpoints de l'API")
url = "http://localhost:8000"
st.write(f"Pour accéder aux différents endpoints de l'API, vous pouvez utiliser l'URL suivante : {url}")
st.write("### Entraînement du modèle")
st.write("Cet endpoint permet d'entraîner le modèle de Logistic Regression en lui fournissant un fichier CSV contenant les données des matchs de football.")

st.write("##### `[POST] /training`")
st.write({
    "file": "Fichier CSV contenant les données des matchs de football"
})

st.write("### Prédiction du résultat d'un match")
st.write("Cet endpoint permet de prédire le résultat d'un match de football en fonction des équipes qui s'affrontent.")

st.write("##### `[POST] /predict`")
st.write({
    "team1": "France",
    "team2": "Germany"
})

st.write("### Appel à l'API OpenAI")
st.write("Cet endpoint permet d'appeler l'API OpenAI pour poser une question sur le match choisit.")

st.write("##### `[GET] /model?text=Hello`")

