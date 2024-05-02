# AJ Grant
# DBManager.py
# Communicates manages the storage and retrieval of fine-tuning datasets


import json
import os
import app.key as key


def addDocument(dataName: str, dataContent: str):
    """
    This function receives the training data for the LLM.
    
    Args:
        dataName (str): The name of the LLM
        dataContent (dict): The training data to save to the database

    Returns:
        str: A message indicating the success or failure of the operation
    """

    f = open(key.datasets_location + dataName + ".json", "a")
    # Add datacontent to the .json as a new line
    f.write(dataContent)
    f.close()

    return "Dataset saved successfully"
        

def deleteEntry(LLMname: str, index: str): #TODO
    """
    This function deletes a document from the training data.
    
    Args:
        LLMname (str): The name of the LLM
        title (str): The title of the document to delete
        
    Returns:
        str: A message indicating the success or failure of the operation
    """
            
    pass 

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