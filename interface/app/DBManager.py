# AJ Grant
# 2024-05-01
# DBManager.py
# Communicates manages the storage and retrieval of fine-tuning datasets


import json
import os
import app.key as key
from werkzeug.utils import secure_filename


def addDocument(dataName: str, file):
    """
    This function saves the training data for the LLM.

    Args:
        dataName (str): The name of the LLM
        file (FileStorage): The file containing the training data

    Returns:
        str: A message indicating the success or failure of the operation
    """
    file_path = key.datasets_location + secure_filename(dataName) + ".json"

    try:
        with open(file_path, 'wb') as f:  # 'wb' for writing in binary mode
            f.write(file.read())  # Read and write the entire file content
    except Exception as e:
        return f"An error occurred: {e}"

    return "Dataset saved successfully"


def deleteDataSet(LLMname: str): #TODO
    """
    This function deletes the table associated with the LLM.
    
    Args:
        LLMname (str): The name of the LLM
        
    Returns:
        str: A message indicating the success or failure of the operation
    """
    pass

def checkDataset(dataName: str):
    """
    This function checks if a dataset exists in the database.

    Args:
        dataName (str): The name of the dataset

    Returns:
        bool: True if the dataset exists, False otherwise
    """
    # Check if the dataset exists in the database and return it's location
    if os.path.exists(key.datasets_location + dataName + ".json"):
        return True
    else:
        return False