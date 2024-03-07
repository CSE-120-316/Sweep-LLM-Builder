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
    return f.createLLM(request.form['name'], request.form['model'])

# Route for LLM training data
@app.route('/trainingData', methods=['POST'])
def trainingData():
    """
    This function receives the training data for the LLM.
    Given the name of the LLM, it saves the training data to a Postgres table.
    """
    return f.saveTrainingData(request.form['name'], request.form['title'], request.form['text'])

# Route to begin LLM training
@app.route('/trainLLM', methods=['POST'])
def trainLLM():
    """
    This function begins the training of the LLM.
    """
    return "LLM training has begun."

# Route to message the LLM
@app.route('/messageLLM', methods=['POST'])
def messageLLM():
    """
    This function sends a message to the LLM.
    """
    return f.messageLLM(request.form['name'], request.form['message'])

# Route to check status
@app.route('/checkStatus', methods=['GET'])
def checkStatus():
    """
    This function checks the status of the LLM.
    """
    return "LLM status: " + f.checkStatus(request.args['name'])


# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
