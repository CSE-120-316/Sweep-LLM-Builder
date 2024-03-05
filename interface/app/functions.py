import pickle
from flask import request
import os
import LLM
import DBManager

def createLLM(name: str, model: str):
    """
    This function creates a new LLM given a name and specified model.
    It saves the LLM instance to a file using pickle.
    """
    llm = LLM(name, model)

    # Establishes the directory to save the LLM object
    directory = "llms"
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save the LLM object to a pickle file
    #TODO: Handles errors such as file already exists, etc.
    with open(f"{directory}/{name}.pkl", "wb") as f:
        pickle.dump(llm, f)

def saveTrainingData(LLMname: str, title: str, text: str):
    """
    This function receives the training data for the LLM.
    Given the name of the LLM, it saves the training data to a Postgres table.
    """

    #Check if an LLM with the given name exists
    try:
        with open(f"llms/{LLMname}.pkl", "rb") as f:
            llm = pickle.load(f)
    except FileNotFoundError:
        return "LLM not found."
    
    # Connect to the database
    DBManager = DBManager()
    
    # Check if a table exists for the LLM
    DBManager.cur.execute(f"SELECT * FROM information_schema.tables WHERE table_name='{LLMname}'")
    if not DBManager.cur.fetchone():
        # If not, create a new table
        DBManager.cur.execute(f"CREATE TABLE {LLMname} (data TEXT)")
    # Save the training data to the table
    DBManager.cur.execute(f"INSERT INTO {LLMname} (data) VALUES ('{title} {text}')")
    DBManager.conn.commit()
    return "Training data received."