from flask import Flask, jsonify, request

# Initialize the Flask app
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return "Hello, welcome to my chatbot!"

# Define a route for the chatbot endpoint (you can expand this later)
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    # Here, you'll process the input and get a response from your model
    response = "You said: " + user_input
    return jsonify({"response": response})

