import dill
from flask import request
import os
import app.LanguageModel as lm
import app.DBManager as dbm

pickle_data = "/app/pickle-data/"
# pickle_data = "/Users/ajgrant/GitHub/_University Courses/Sweep-LLM-Builder/volumes/pickle-data"

def LoadLLM(name: str):
    """
    This function loads the LLM instances from the pickle files.
    """
    with open(pickle_data  + name + ".pkl", "rb") as f:
        llm = dill.load(f)

    return llm

def createLLM(name: str, model: str):
    """
    This function creates a new LLM given a name and specified model.
    It saves the LLM instance to a file using pickle.
    """
    llm = lm.LM(name, model)
    # Save the LLM object to a pickle file
    #TODO: Handles errors such as LLM name already exists, etc.
    return llm


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