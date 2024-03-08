import dill
from flask import request
import os
import app.LanguageModel as lm
import app.DBManager as dbm

# pickle_data = "/app/pickle-data/"
pickle_data = "/Users/ajgrant/GitHub/_University Courses/Sweep-LLM-Builder/volumes/pickle-data/"

def LoadLLM(name: str):
    """
    This function loads the LLM instances from the pickle files.
    """
    # Load the LLM object from a pickle file
    with open(pickle_data + name + ".pkl", "rb") as f:
        llm = dill.load(f)
    
    # Readd the client to the LLM object
    #! This is an OpenAI thing that won't be in the final version
    llm.client = lm.OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

    return llm

def SaveLLM(llm: lm.LM):
    """
    This function saves the LLM instance to a file using pickle.
    """
    # Remove sensitive information from the LLM object 
    #!This is an OpenAI thing that won't be in the final version
    llm.client = None 

    # Save the LLM object to a pickle file
    with open(pickle_data + llm.name + ".pkl", "wb") as f:
        dill.dump(llm, f)

def createLLM(name: str, model: str):
    """
    This function creates a new LLM given a name and specified model.
    It saves the LLM instance to a file using pickle.
    """
    llm = lm.LM(name, model)
    # Save the LLM object to a pickle file
    #TODO: Handles errors such as LLM name already exists, etc.

    SaveLLM(llm)
    return llm.name + " LLM created with model " + llm.model + "."


def saveTrainingData(LLMname: str, question: str, answer: str):
    """
    This function receives the training data for the LLM.
    Given the name of the LLM, it saves the training data to a Postgres table.

    Args:
        LLMname (str): The name of the LLM
        question (str): The question to be added to the training data
        answer (str): The associated answer to the question
    """

    try:
        llm = LoadLLM(LLMname)
    except:
        return "LLM not found."

    # Connect to the database
    import app.DBManager as dbm

    DBManager = dbm.DBManager()

    try:
        # Save the training data to the table
        DBManager.addDocument(LLMname, question, answer)
        return "Question/answer pair added to " + LLMname + " training data."
    except Exception as e: #TODO Test this
        return e
    
def trainLLM(name: str):
    """
    This function begins the training of the LLM.
    It retrieves the training data from the database and trains the model.

    Args:
        name (str): The name of the LLM
    """
    try:
        llm = LoadLLM(name)
    except:
        return "LLM not found."

    # Connect to the database
    import app.DBManager as dbm

    DBManager = dbm.DBManager()

    # Get the training data
    training_data = DBManager.getTrainingData(name)

    # Train the model
    llm.train(training_data)

    # Save the LLM object to a pickle file
    with open(pickle_data + name + ".pkl", "wb") as f:
        dill.dump(llm, f)

    return "LLM training has begun."
    
def checkStatus(name: str):
    """
    This function checks the status of the LLM.

    Args:
        name (str): The name of the LLM

    Returns:
        str: A message indicating the status of the LLM
    """
    try:
        llm = LoadLLM(name)
    except:
        return "LLM not found."
    
    return llm.status