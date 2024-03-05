import pickle
from flask import request
import os
import app.LanguageModel as lm
import app.DBManager as dbm

pickle_data = "/app/pickle-data"

def createLLM(name: str, model: str):
    """
    This function creates a new LLM given a name and specified model.
    It saves the LLM instance to a file using pickle.
    """
    llm = lm.LM(name, model)

    # Establishes the directory to save the LLM object
    if not os.path.exists(pickle_data):
        os.makedirs(pickle_data)

    # Save the LLM object to a pickle file
    #TODO: Handles errors such as file already exists, etc.
    with open(f"{pickle_data}/{name}.pkl", "wb") as f:
        pickle.dump(llm, f)

    return llm.name + " created." + "Status: " + llm.status




def saveTrainingData(LLMname: str, title: str, text: str):
    """
    This function receives the training data for the LLM.
    Given the name of the LLM, it saves the training data to a Postgres table.
    """

    #Check if an LLM with the given name exists
    try:
        with open(f"{pickle_data}/{LLMname}.pkl", "rb") as f:
            llm = pickle.load(f)
    except FileNotFoundError:
        return "LLM not found."
    
    # Connect to the database
    DBManager = dbm.DBManager()
    
    # Check if the table already exists
    DBManager.cur.execute(f"SELECT to_regclass('{LLMname}')")
    if not DBManager.cur.fetchone()[0]:
        # If not, create a new table
        DBManager.cur.execute(f"CREATE TABLE {LLMname} (title TEXT, contents TEXT)")
        print(f"Table {LLMname} not found, creating new table.")
    # Save the training data to the table
    DBManager.cur.execute(f"INSERT INTO {LLMname} (title, contents) VALUES (%s, %s)", (title, text))
    DBManager.conn.commit()
    DBManager.cur.close()

    print("{title} saved to {LLMname} table.")
    return "Training data received."