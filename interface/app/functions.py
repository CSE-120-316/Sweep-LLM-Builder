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

def deleteChatBot(name: str):
    """
    This function deletes the LLM instance from the pickle files.
    """
    # Delete the LLM object from a pickle file
    os.remove(pickle_data + name + ".pkl")

    return "LLM deleted successfully"

def deleteDataset(name: str):
    """
    This function deletes the dataset from the file system.
    """
    # Delete the dataset from the file system
    os.remove(llm_datasets + name + ".json")

    return "Dataset deleted successfully"

def deleteEverything():
    """
    This function deletes all the LLM instances and datasets.
    """
    # Delete all the LLM objects from the pickle files
    chatbot_files = os.listdir(pickle_data)
    for file in chatbot_files:
        os.remove(pickle_data + file)

    # Delete all the datasets from the file system
    dataset_files = os.listdir(llm_datasets)
    for file in dataset_files:
        os.remove(llm_datasets + file)
            
    return "All LLMs and datasets have been deleted."

def createChatBot(name: str, lr: str):
    """
    This function creates a new LLM given a name and specified model.
    It saves the LLM instance to a file using pickle.
    """
    chatbot = cb.ChatBot(name, lr)
    # Save the LLM object to a pickle file
    #TODO: Handles errors such as LLM name already exists, etc.

    saveChatBot(chatbot)

    message = {
        "name": chatbot.name,
        "lr": chatbot.lr,
        "status": chatbot.status
    }
    return message

def uploadTrainingData(dataName: str, file):
    """
    This function receives the training data for the LLM as a file.
    Given the name of the LLM, it saves the training data to the appropriate storage.

    Args:
        dataName (str): The name of the LLM
        file (FileStorage): The file containing the training data
    """
    try:
        # Save the training data to the table or file system
        return dbm.addDocument(dataName, file)
    except Exception as e:
        return str(e)  # Ensure the message is stringified for proper handling

    
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
        print(e)
        return e
    
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

def listDatasets():
    """
    This function lists all the datasets.
    """
    # Get all the datasets
    datasets = dbm.listDatasets()

    # From the list of datasets, extract the names by removing the file extension (.json)
    datasets = [dataset[:-5] for dataset in datasets]

    return datasets

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
        "lr": llm.lr,
        "status": llm.status
        }
    except:
        info = {
            "name": name,
            "lr": "N/A",
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
        chatbot = loadChatBot(name)
    except:
        return "LLM not found"

    message = chatbot.message(message)
    
    # Extract message
    message = message[0]
    
    # Remove text behind "[/INST]  "
    message = message.split("[/INST]  ")[1]

    return message