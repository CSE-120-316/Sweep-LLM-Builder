import dill
from flask import request
import os
import app.ChatBot as cb
import app.DBManager as dbm

pickle_data = "/app/pickle-data/"
llm_datasets = "/app/llm-datasets/"

def loadChatBot(name: str):
    """
    This function loads the LLM instances from the pickle files.
    """
    # Load the LLM object from a pickle file
    with open(pickle_data + name + ".pkl", "rb") as f:
        chatbot = dill.load(f)

    return chatbot

def saveChatBot(chatbot: cb.ChatBot):
    """
    This function saves the LLM instance to a file using pickle.
    """
    # Save the LLM object to a pickle file
    with open(pickle_data + cb.name + ".pkl", "wb") as f:
        dill.dump(chatbot, f)

def createChatBot(name: str, model: str):
    """
    This function creates a new LLM given a name and specified model.
    It saves the LLM instance to a file using pickle.
    """
    chatbot = cb.ChatBot(name, model)
    # Save the LLM object to a pickle file
    #TODO: Handles errors such as LLM name already exists, etc.

    saveChatBot(chatbot)
    return "creation success"


def saveTrainingData(dataName: str, dataContent: str):
    """
    This function receives the training data for the LLM.
    Given the name of the LLM, it saves the training data to a Postgres table.

    Args:
        dataName (str): The name of the LLM
        dataContent (dict): The training data to save to the database
    """

    # Connect to the database
    DBManager = dbm.DBManager()

    try:
        # Save the training data to the table
        DBManager.addDocument(dataName, dataContent)
        return "Dataset saved successfully"
    except Exception as e: #TODO Test this
        return e
    
def trainLLM(name: str, system_message: str = ""):
    """
    This function begins the training of the LLM.
    It retrieves the training data from the database and trains the model.

    Args:
        name (str): The name of the LLM
    """
    try:
        llm = loadChatBot(name)
    except:
        return "LLM not found."

    # Train the model
    if system_message == "":
        llm.train()
    else:
        llm.train(system_message)
        
    # Save the LLM object to a pickle file
    saveChatBot(llm)

    return "LLM training has begun"
    
def getInfo(name: str):
    """
    This function checks the status of the LLM.

    Args:
        name (str): The name of the LLM

    Returns:
        str: A message indicating the status of the LLM
    """
    try:
        llm = loadChatBot(name)
        info = {
        "name": llm.name,
        "model": llm.model,
        "status": llm.status
        }
    except:
        info = {
            "name": name,
            "model": "N/A",
            "status": "LLM not found"
        }

    return info

def messageLLM(name: str, message: str):
    """
    This function sends a message to the LLM.

    Args:
        name (str): The name of the LLM
        message (str): The message to send to the LLM

    Returns:
        str: The response from the LLM
    """
    try:
        llm = loadChatBot(name)
    except:
        return "LLM not found"

    return llm.message(message)