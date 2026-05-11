from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Charger le modèle
model = joblib.load("models/london_weather_model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        # récupérer les données du formulaire
        cloud_cover = float(request.form["cloud_cover"])
        sunshine = float(request.form["sunshine"])
        global_radiation = float(request.form["global_radiation"])
        max_temp = float(request.form["max_temp"])
        min_temp = float(request.form["min_temp"])
        precipitation = float(request.form["precipitation"])
        pressure = float(request.form["pressure"])
        snow_depth = float(request.form["snow_depth"])
        year = int(request.form["year"])
        month = int(request.form["month"])
        day = int(request.form["day"])

        # créer DataFrame (IMPORTANT)
        data = pd.DataFrame({
            "cloud_cover": [cloud_cover],
            "sunshine": [sunshine],
            "global_radiation": [global_radiation],
            "max_temp": [max_temp],
            "min_temp": [min_temp],
            "precipitation": [precipitation],
            "pressure": [pressure],
            "snow_depth": [snow_depth],
            "year": [year],
            "month": [month],
            "day": [day]
        })

        # prédiction
        prediction = model.predict(data)[0]

    return render_template("indexwth.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)