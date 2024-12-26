from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    song1 = request.form["song1"]
    # song2 = request.form["song2"]

    # Prepare the request data
    data = {"songs": [song1]}

    try:
        response = requests.post(
            "http://localhost:52049/api/recommend",
            json=data,
            headers={"Content-Type": "application/json"},
        )
        response.raise_for_status()  # Raise exception for non-200 status codes
        recommendations = response.json()["songs"]
        return render_template("recommendations.html", recommendations=recommendations)
    except requests.exceptions.RequestException as e:
        return f"Error: {e}", 500  # Internal Server Error

if __name__ == "__main__":
    app.run(debug=True)