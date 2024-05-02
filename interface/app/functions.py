# AJ Grant
# 2024-05-01
# functions.py
# Communicates with the chatbots, database manager, and the Flask routes, connecting everything together.

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
    with open(pickle_data + chatbot.name + ".pkl", "wb") as f:
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

    message = {
        "name": chatbot.name,
        "model": chatbot.model,
        "status": chatbot.status
    }
    return message

def uploadTrainingData(dataName: str, dataContent: str):
    """
    This function receives the training data for the LLM.
    Given the name of the LLM, it saves the training data to a Postgres table.

    Args:
        dataName (str): The name of the LLM
        dataContent (dict): The training data to save to the database
    """


    try:
        # Save the training data to the table
        dbm.addDocument(dataName, dataContent)
    except Exception as e: #TODO Test this
        return e
    
    return "Data uploaded successfully"

def trainChatBot(name: str, data_set: str = ""):
    """
    This function begins the training of the LLM.
    It retrieves the training data from the database and trains the model.

    Args:
        name (str): The name of the LLM
    """
    try:
        chatbot = loadChatBot(name)
    except:
        return "LLM not found."

    # Train the model
    try:
        chatbot.train(data_set)
    except Exception as e:
        return e
    
    chatbot.status = "Trained"
    # Save the LLM object to a pickle file
    saveChatBot(chatbot)

    return getInfo(name)

def listChatBots(status: str): #! TEST THIS
    """
    This function lists the names of all the ChatBots with a given status.

    Args:
        status (str): Untrained, Training, Trained, or All
    """
    # Get all the ChatBots
    chatbot_files = os.listdir(pickle_data)
    chatbots = []
    for file in chatbot_files:
        with open(pickle_data + file, "rb") as f:
            chatbot = dill.load(f)
            chatbots.append(chatbot)

    # Filter the ChatBots by status
    if status == "All":
        names = [chatbot.name for chatbot in chatbots]
    else:
        names = [chatbot.name for chatbot in chatbots if chatbot.status == status]

    return names

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