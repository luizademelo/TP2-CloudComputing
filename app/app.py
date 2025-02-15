from flask import Flask, jsonify, request, render_template
from datetime import datetime

app = Flask(__name__)


import pickle
from model import compute_rules

@app.route('/')
def home():
   return render_template("index.html")

@app.route("/api/recommend", methods=["POST"])
def recommend(): 
    data = request.json
    compute_rules(data) 
    app.model = pickle.load(open("data/rules.pickle", "rb"))


    recommendations = app.model
    return jsonify({"songs": recommendations, "version": "2.0.0", "model_date": datetime.now().strftime("%Y-%m-%d")})

if __name__ == "__main__":
    app.run(host='0.0.0.0')