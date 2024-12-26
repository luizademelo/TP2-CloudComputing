from flask import Flask, jsonify, request
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
    compute_rules() 
    app.model = pickle.load(open("rules.pickle", "rb"))


    recommendations = app.model['consequents'].tolist() 
    return jsonify({"songs": recommendations})

if __name__ == "__main__":
    app.run(host='0.0.0.0')