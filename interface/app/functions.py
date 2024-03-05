import pickle
from flask import request
import psycopg2

class LLM:
    def __init__(self, name: str, model: str):
        self.name = name
        self.model = model
        self.training_data = None
        self.status = None

    def message():
        pass

    def train():
        pass

    def check_status():
        pass

def createLLM(name: str, model: str):
    """
    This function creates a new LLM given a name and specified model.
    It saves the LLM instance to a file using pickle.
    """
    llm = LLM(name, model)
    with open(f"llms/{name}.pkl", "wb") as f:
        pickle.dump(llm, f)

class DBManager:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="llm",
            user="user",
            password="pass",
            host="localhost",
            port="5432"
        )
        self.cur = self.conn.cursor()

DBManager = DBManager()

def saveTrainingData(LLMname: str, title: str, text: str):
    """
    This function receives the training data for the LLM.
    Given the name of the LLM, it saves the training data to a Postgres table.
    """
    # Check if a table exists for the LLM
    DBManager.cur.execute(f"SELECT * FROM information_schema.tables WHERE table_name='{LLMname}'")
    if not DBManager.cur.fetchone():
        # If not, create a new table
        DBManager.cur.execute(f"CREATE TABLE {LLMname} (data TEXT)")
    # Save the training data to the table
    DBManager.cur.execute(f"INSERT INTO {LLMname} (data) VALUES ('{title} {text}')")
    DBManager.conn.commit()