import streamlit as st
import requests

# Titre de la page
st.title("Upload CSV et Entraînement du Modèle")

# Téléchargement du fichier CSV
uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")

# URL de l'API FastAPI
api_train_url = "http://localhost:8000/training"
api_predict_url = "http://localhost:8000/predict"
api_model_url = "http://localhost:8000/model"

if uploaded_file is not None:
    # Affichage du fichier CSV
    st.write("Fichier CSV chargé :")
    # Bouton pour envoyer le fichier à l'API
    if st.button("Entraîner le modèle"):
        # Envoi du fichier CSV à l'API FastAPI
        files = {'file': (uploaded_file.name, uploaded_file, 'text/csv')}
        response = requests.post(api_train_url, files=files)

        # Affichage du score de l'entraînement
        if response.status_code == 200:
            result = response.json()
            st.success(f"Entraînement terminé avec un score de : {result['score']}")
        else:
            st.error("Erreur lors de l'entraînement du modèle.")

# Liste des équipes
teams = [
    "Abkhazia", "Afghanistan", "Albania", "Alderney", "Algeria", "American Samoa",
    "Andorra", "Angola", "Anguilla", "Antigua and Barbuda", "Argentina", "Armenia",
    "Aruba", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain",
    "Bangladesh", "Barbados", "Basque Country", "Belarus", "Belgium", "Belize",
    "Benin", "Bermuda", "Bhutan", "Bolivia", "Bonaire", "Bosnia and Herzegovina",
    "Botswana", "Brazil", "British Virgin Islands", "Brunei", "Bulgaria", "Burkina Faso",
    "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Cayman Islands",
    "Central African Republic", "Chad", "Chile", "China PR", "Colombia", "Comoros",
    "Congo", "Cook Islands", "Costa Rica", "Crimea", "Croatia", "Cuba", "Curaçao",
    "Cyprus", "Czech Republic", "DR Congo", "Denmark", "Djibouti", "Dominica",
    "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador", "England",
    "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Falkland Islands",
    "Faroe Islands", "Fiji", "Finland", "France", "French Guiana", "Frøya", "Gabon",
    "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", "Gozo", "Greece", "Greenland",
    "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guernsey", "Guinea", "Guinea-Bissau",
    "Guyana", "Haiti", "Honduras", "Hong Kong", "Hungary", "Iceland", "India",
    "Indonesia", "Iran", "Iraq", "Iraqi Kurdistan", "Isle of Man", "Isle of Wight",
    "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jersey", "Jordan", "Kazakhstan",
    "Kenya", "Kernow", "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan", "Kárpátalja",
    "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein",
    "Lithuania", "Luxembourg", "Macau", "Madagascar", "Malawi", "Malaysia", "Maldives",
    "Mali", "Malta", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico",
    "Moldova", "Monaco", "Mongolia", "Montenegro", "Montserrat", "Morocco", "Mozambique",
    "Myanmar", "Namibia", "Nepal", "Netherlands", "New Caledonia", "New Zealand",
    "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia", "Northern Cyprus",
    "Northern Ireland", "Northern Mariana Islands", "Norway", "Occitania", "Oman",
    "Orkney", "Padania", "Pakistan", "Palestine", "Panama", "Panjab", "Papua New Guinea",
    "Paraguay", "Parishes of Jersey", "Peru", "Philippines", "Poland", "Portugal",
    "Provence", "Puerto Rico", "Qatar", "Republic of Ireland", "Rhodes", "Romania",
    "Russia", "Rwanda", "Réunion", "Saint Barthélemy", "Saint Kitts and Nevis",
    "Saint Lucia", "Saint Martin", "Saint Vincent and the Grenadines", "Samoa",
    "San Marino", "Saudi Arabia", "Scotland", "Sealand", "Senegal", "Serbia", "Seychelles",
    "Shetland", "Sierra Leone", "Singapore", "Sint Maarten", "Slovakia", "Slovenia",
    "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Ossetia",
    "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland",
    "Syria", "Székely Land", "São Tomé and Príncipe", "Tahiti", "Taiwan", "Tajikistan",
    "Tanzania", "Thailand", "Tibet", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago",
    "Tunisia", "Turkey", "Turkmenistan", "Turks and Caicos Islands", "Tuvalu", "Uganda",
    "Ukraine", "United Arab Emirates", "United States", "United States Virgin Islands",
    "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Wales",
    "Western Isles", "Western Sahara", "Yemen", "Ynys Môn", "Yorkshire", "Zambia",
    "Zanzibar", "Zimbabwe", "Åland"
]

# Section de prédiction de match
st.header("Prédiction de Match")
team1 = st.selectbox("Sélectionnez l'équipe 1", teams)
team2 = st.selectbox("Sélectionnez l'équipe 2", teams)

if st.button("Prédire le match"):
    if team1 and team2:
        data = {
            "team1": team1,
            "team2": team2
        }
        response = requests.post(api_predict_url, json=data)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Prédiction : {result['winner']} va probablement gagner avec un score de prédiction de {result['prediction_score']}")
        else:
            st.error("Erreur lors de la prédiction du match.")

# Section de questions sur le match
st.header("Poser une question sur le match")
question = st.text_input("Entrez votre question sur le match")

if st.button("Poser la question"):
    if team1 and team2 and question:
        full_question = f"{question} (Match: {team1} vs {team2})"
        params = {"text": full_question}
        response = requests.get(api_model_url, params=params)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Réponse : {result['response']}")
        else:
            st.error("Erreur lors de l'envoi de la question.")