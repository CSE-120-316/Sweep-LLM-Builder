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
    f.createLLM(request.form['name'], request.form['model'])
    return "LLM created."

# Route for LLM training data
@app.route('/trainingData', methods=['POST'])
def trainingData():
    """
    This function receives the training data for the LLM.
    Given the name of the LLM, it saves the training data to a Postgres table.
    """
    f.saveTrainingData(request.form['name'], request.form['title'], request.form['text'])
    return "Training data received."

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
    return "Message sent to LLM."

# Route to check status
@app.route('/checkStatus', methods=['GET'])
def checkStatus():
    """
    This function checks the status of the LLM.
    """
    return "Status: OK"


# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
