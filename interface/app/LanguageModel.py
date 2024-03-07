import pickle
import DBManager as dbm
from openai import OpenAI

class LM:
    def __init__(self, name: str, model: str):
        self.name = name
        self.model = model
        self.training_data = None
        self.status = "Untrained"

        #! The following is CHATGPT specific stuff. This will look very different
        #! when we implement our own local language model.
        self.client = OpenAI()
        
        self.messages = []


    def message():
        pass

    def train(self):
        #! This will look very different when we implement our own local language model.

        db = dbm.DBManager()

        messages = [{"role": "system", "content": "You are a helpful assistant. That answers questions about provided documents."},]
        training_data = db.getTrainingData(self.name)
        

        self.status = "Trained"

        pass

    def check_status(name: str):
        # Get the LLm from pickle file and return its status
        with open(f"llms/{name}.pkl", "rb") as f:
            llm = pickle.load(f)
        return llm.status
