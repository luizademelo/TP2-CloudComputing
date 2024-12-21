from flask import Flask, jsonify, request
from recomender import compute_rules
import pickle

app = Flask(__name__)

@app.route("/api/recommend", methods=["POST"])

def recommend(): 
    compute_rules() 
    app.model = pickle.load(open("rules.pickle", "rb"))


    recommendations = app.model['consequents'].tolist() 
    return jsonify({"songs": recommendations})

if __name__ == "__main__":
    app.run()