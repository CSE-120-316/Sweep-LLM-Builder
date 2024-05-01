from flask import Flask, request
import app.functions as f
import torch

# Create Flask application instance
app = Flask(__name__)

# Route for LLM training data !JSON STUFF GOES HERE ASHLEY :)
@app.route('/trainingData', methods=['POST'])
def trainingData():
    """
    This function receives the training data for the LLM.
    Given the name of the data, it saves the training data to a Postgres table.
    """
    message = f.saveTrainingData(request.form['data_name'], request.form['data_content'])
    response = {
        "dataSet": "data_name",
        "message": message
    }
    return response

# Route for LLM selection
@app.route('/createChatBot', methods=['POST'])
def createChatBot():
    """
    This function creates a new ChatBot given a name and specified model.
    """
    message = f.createChatBot(request.form['name'], request.form['model'])
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
        "LLM": f.getInfo(request.form['name']),
        "message": message
    }
    return response

# Route to message the LLM
@app.route('/messageChatBot', methods=['POST'])
def messageLLM():
    """
    This function sends a message to the LLM.
    """
    message = f.messageLLM(request.form['name'], request.form['message'])
    response = {
        "LLM": f.getInfo(request.form['name']),
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

@app.route('/ping', methods=['GET'])
def ping():
    """
    This function checks the status of the server.
    """
    return str(torch.cuda.is_available())



# Main function
if __name__ == '__main__':
    app.run(debug=True)
