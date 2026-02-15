from flask import Flask, render_template, request
import pickle
import json
import numpy as np

app = Flask(__name__)

with open("Iris_knn.pkl", "rb") as f:
    knn_model = pickle.load(f)

with open("Iris_nb.pkl", "rb") as f:
    nb_model = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html", prediction=None, metrics=None)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        sepal_length = float(request.form["sepal_length"])
        sepal_width = float(request.form["sepal_width"])
        petal_length = float(request.form["petal_length"])
        petal_width = float(request.form["petal_width"])
        model_choice = request.form["model"]

        features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

        if model_choice == "knn":
            prediction = knn_model.predict(features)[0]
            json_file = "Iris_knn_Testperofrmace.json"
        else:
            prediction = nb_model.predict(features)[0]
            json_file = "Iris_nb_Testperofrmace.json"

        # Convert numeric to flower name
        flower_map = {
            0: "Setosa",
            1: "Versicolor",
            2: "Virginica"
        }

        prediction = flower_map.get(int(prediction))

        with open(json_file, "r") as f:
            metrics = json.load(f)

        return render_template(
            "index.html",
            prediction=prediction,
            metrics=metrics,
            selected_model=model_choice
        )

    except Exception as e:
        return render_template("index.html", error=str(e), prediction=None, metrics=None)


if __name__ == "__main__":
    app.run(debug=True)
