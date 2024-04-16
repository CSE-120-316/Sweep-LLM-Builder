import json
import os
import app.key as key


def addDocument(self, dataName: str, dataContent: str):
    """
    This function receives the training data for the LLM.
    
    Args:
        dataName (str): The name of the LLM
        dataContent (dict): The training data to save to the database

    Returns:
        str: A message indicating the success or failure of the operation
    """

    f = open(key.datasets_location + dataName + ".json", "w")
    # Add datacontent to the .json as a new line
    f.write(dataContent + "\n")
    f.close()

    return "Dataset saved successfully"
        

def deleteEntry(self, LLMname: str, index: str): #TODO
    """
    This function deletes a document from the training data.
    
    Args:
        LLMname (str): The name of the LLM
        title (str): The title of the document to delete
        
    Returns:
        str: A message indicating the success or failure of the operation
    """
            
    pass 

def deleteDataSet(self, LLMname: str): #TODO
    """
    This function deletes the table associated with the LLM.
    
    Args:
        LLMname (str): The name of the LLM
        
    Returns:
        str: A message indicating the success or failure of the operation
    """
    pass

def checkDataset(self, dataName: str):
    """
    This function checks if a dataset exists in the database.

    Args:
        dataName (str): The name of the dataset

    Returns:
        bool: True if the dataset exists, False otherwise
    """
    # Check if the dataset exists in the database and return it's location
    if os.path.exists(key.datasets_location + dataName + ".json"):
        return str(key.datasets_location + dataName + ".json")
    else:
        return None