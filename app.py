# app.py
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from chatbot_logic import get_response

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def chatbot_response():
    user_input = request.json['message']
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
