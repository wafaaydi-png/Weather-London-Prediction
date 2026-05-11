# 🌦️ Prédiction de la Température à Londres avec Machine Learning

## 📌 Description du projet

Ce projet consiste à développer une application web interactive permettant de **prédire la température à Londres** à partir de plusieurs variables climatiques.

L’application utilise un modèle de **Machine Learning** entraîné sur des données météorologiques historiques de Londres et déployé avec **Flask**.

L’utilisateur peut saisir les données climatiques dans une interface web intuitive pour obtenir instantanément une prédiction de température.

---

## 🎯 Objectif

Prédire la température à partir des variables météorologiques suivantes :

- ☁️ Couverture nuageuse (*Cloud Cover*)
- ☀️ Ensoleillement (*Sunshine*)
- 🌞 Rayonnement global (*Global Radiation*)
- 🌡️ Température maximale (*Max Temperature*)
- ❄️ Température minimale (*Min Temperature*)
- 🌧️ Précipitations (*Precipitation*)
- 📈 Pression atmosphérique (*Pressure*)
- ⛄ Profondeur de neige (*Snow Depth*)
- 📅 Date (Année, Mois, Jour)

---

## 🤖 Modèles Machine Learning testés

Trois modèles de régression ont été entraînés et évalués avec la métrique **RMSE** :

| Modèle | RMSE |
|--------|------|
| Linear Regression | 0.8737 |
| Random Forest Regressor | 0.8562 |
| Gradient Boosting Regressor | **0.8335** |

✅ **Le modèle Gradient Boosting a obtenu la meilleure performance et a été choisi pour le déploiement.**

---

## 🛠️ Technologies utilisées

### Backend
- Python
- Flask
- Pandas
- Joblib
- Scikit-learn

### Frontend
- HTML5
- CSS3

### Machine Learning
- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor
## 📷 Capture d’écran

![Capture écran](weatherapp.png)


## 💻 Fonctionnalités

✅ Interface web interactive  
✅ Saisie des données climatiques  
✅ Prédiction instantanée de température  
✅ Design moderne avec image de fond météo  
✅ Modèle Machine Learning déployé avec Flask  

---




