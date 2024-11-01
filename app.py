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

# New route to handle Dialogflow webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    # Parse the request from Dialogflow
    req = request.get_json(silent=True, force=True)
    intent = req.get('queryResult').get('intent').get('displayName')
    
    # Define responses based on different intents
    if intent == "Branch Information":
        response_text = "Our college offers branches in CSE, AIML, IOT, DS, IT, MECH, CIVIL, ECE, and EEE."
    elif intent == "Fee Structure":
        response_text = "The fee structure varies by branch and scholarship status. Visit our website or contact admissions for detailed information."
    elif intent == "College Location":
        response_text = "Our college is located in Malakpet, Hyderabad, Telangana."
    else:
        # Fallback if intent is not matched
        response_text = get_response(req.get('queryResult').get('queryText'))
    
    # Send the response back to Dialogflow
    return jsonify({"fulfillmentText": response_text})

if __name__ == '__main__':
    app.run(debug=True)
