from flask import Flask, request
import app.functions as f

# Create Flask application instance
app = Flask(__name__)

# Route for LLM selection
@app.route('/createLLM', methods=['POST'])
def createLLM():
    """
    This function creates a new LLM given a name and specified model.
    """
    message = f.createLLM(request.form['name'], request.form['model'])
    response = {
        "LLM": f.getInfo(request.form['name']),
        "message": message
    }
    return response
    
# Route for LLM training data
@app.route('/trainingData', methods=['POST'])
def trainingData():
    """
    This function receives the training data for the LLM.
    Given the name of the LLM, it saves the training data to a Postgres table.
    """
    message = f.saveTrainingData(request.form['name'], request.form['question'], request.form['answer'])
    response = {
        "LLM": f.getInfo(request.form['name']),
        "message": message
    }
    return response

# Route to begin LLM training
@app.route('/trainLLM', methods=['POST'])
def trainLLM():
    """
    This function begins the training of the LLM.
    """
    message = f.trainLLM(request.form['name'], request.form['system_message'])
    response = {
        "LLM": f.getInfo(request.form['name']),
        "message": message
    }
    return response

# Route to message the LLM
@app.route('/messageLLM', methods=['POST'])
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
    return "pong"

# Main function
if __name__ == '__main__':
    app.run(debug=True)
