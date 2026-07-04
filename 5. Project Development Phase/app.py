from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# ==========================================
# Load Saved Model and Scaler
# ==========================================

model = joblib.load("saved_models/flood_model.joblib")
scaler = joblib.load("saved_models/scaler.joblib")


# ==========================================
# Home Page
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# Prediction Page
# ==========================================

@app.route("/predict")
def predict_page():

    return render_template(
        "predict.html",
        prediction=None,
        result_class=""
    )


# ==========================================
# Prediction Route
# ==========================================

@app.route("/prediction", methods=["POST"])
def prediction():

    try:

        # ==========================
        # Read Form Values
        # ==========================

        temp = float(request.form["temp"])
        humidity = float(request.form["humidity"])
        cloud = float(request.form["cloud"])
        annual = float(request.form["annual"])
        janfeb = float(request.form["janfeb"])
        marmay = float(request.form["marmay"])
        junsep = float(request.form["junsep"])
        octdec = float(request.form["octdec"])
        avgjune = float(request.form["avgjune"])
        sub = float(request.form["sub"])

        # ==========================
        # Create Input Array
        # ==========================

        input_data = np.array([[
            temp,
            humidity,
            cloud,
            annual,
            janfeb,
            marmay,
            junsep,
            octdec,
            avgjune,
            sub
        ]])

        # ==========================
        # Scale Input
        # ==========================

        scaled_data = scaler.transform(input_data)

        # ==========================
        # Predict
        # ==========================

        prediction = model.predict(scaled_data)

        # ==========================
        # Prediction Result
        # ==========================

        if prediction[0] == 1:

            result = "Flood Likely"
            result_class = "danger"

        else:

            result = "No Flood Likely"
            result_class = "safe"

        # ==========================
        # Return Same Page
        # ==========================

        return render_template(
            "predict.html",
            prediction=result,
            result_class=result_class
        )

    except Exception as e:

        return render_template(
            "predict.html",
            prediction=f"Error: {str(e)}",
            result_class="danger"
        )


# ==========================================
# Run Flask
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)