# AJ Grant
# 2024-05-01
# run.py
# Web routes for our application.

from flask import Flask, request
import app.functions as f
import torch
from flask_cors import CORS  # Import CORS

# Create Flask application instance
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and methods


# Route for LLM training data !JSON STUFF GOES HERE ASHLEY :)
@app.route('/trainingDataUpload', methods=['POST'])
def trainingData():
    """
    This function receives the training data for the LLM.
    Given the name of the data, it saves the training data to a Postgres table.
    """

    file = request.files['dataset']
    message = f.uploadTrainingData(request.form['data_name'], file)
    response = {
        "dataSet": "data_name",
        "message": message
    }
    return response

# Route for LLM selection
@app.route('/createChatBot', methods=['POST'])
def createChatBot():
    """
    This function creates a new ChatBot given a name and specified learning rate.
    """
    message = f.createChatBot(request.form['name'], request.form['lr'])
    response = {
        "ChatBot": f.getInfo(request.form['name']),
        "message": message
    }
    return response

# Route to begin LLM training
@app.route('/trainChatBot', methods=['POST'])
def trainChatBot():
    """
    This function begins the training of the ChatBot given the name of 
    a chatbot and the name of the dataset.
    """
    message = f.trainChatBot(request.form['name'], request.form['data_name'])
    response = {
        "ChatBot": f.getInfo(request.form['name']),
        "message": message
    }
    return response

# Route to message the LLM
@app.route('/messageChatBot', methods=['POST'])
def messageChatBot():
    """
    This function sends a message to the LLM.
    """
    message = f.messageLLM(request.form['name'], request.form['message'])
    response = {
        "ChatBot": f.getInfo(request.form['name']),
        "message": message
    }
    return response

# Route to check status
@app.route('/checkStatus', methods=['GET'])
def checkStatus():
    """
    This function checks the status of the LLM.
    """
    response = f.getInfo(request.args['name'])
    return response

# Route to list all ChatBots
@app.route('/listChatBots', methods=['GET'])
def listChatBots():
    """
    This function lists all the ChatBots.

    status (str): Untrained, Training, Trained, All
    """
    response = f.listChatBots(request.args['status'])
    return response

# Route to list datasets
@app.route('/listDatasets', methods=['GET'])
def listDatasets():
    """
    This function lists all the datasets.
    """
    response = f.listDatasets()
    return response

@app.route('/ping', methods=['GET'])
def ping():
    """
    This function checks the status of the server.
    """
    return "pong"


# Main function
if __name__ == '__main__':
    app.run(debug=True)
