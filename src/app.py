from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__, template_folder="../templates")
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    yob = int(data["age"])  # Year of birth
    # Calculate age in years
    age_in_days = yob * 365  # Convert age to days (approximation)

    input_data = pd.DataFrame([{
        "age": age_in_days,
        "height": int(data["height"]),
        "weight": float(data["weight"]),
        "ap_hi": int(data["ap_hi"]),
        "ap_lo": int(data["ap_lo"]),
        "cholesterol": int(data["cholesterol"]),
        "gluc": int(data["gluc"]),
        "smoke": int(data["smoke"]),
        "alco": int(data["alco"]),
        "active": int(data["active"]),
    }])

    prediction = model.predict(input_data)[0]
    print(prediction)
    result = "Likely Healthy (No cardiovascular disease)" if prediction == 0 else "At Risk (Cardiovascular disease detected)"
    
    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
