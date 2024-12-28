from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)


# from recomender import compute_rules
import pickle
from recomender import compute_rules

@app.route('/')
def home():
   return "hello world!"

@app.route("/api/recommend", methods=["POST"])
def recommend(): 
    data = request.json
    compute_rules(data) 
    app.model = pickle.load(open("rules.pickle", "rb"))


    recommendations = app.model
    return jsonify({"songs": recommendations, "version": "1.0.0", "model_date": datetime.now().strftime("%Y-%m-%d")})

if __name__ == "__main__":
    app.run(host='0.0.0.0')