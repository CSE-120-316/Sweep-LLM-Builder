import app.DBManager as dbm
from openai import OpenAI
import os

class LM:
    def __init__(self, name: str, model: str):
        self.name = name
        self.model = model
        self.training_data = None
        self.status = "Untrained"

        #! The following is CHATGPT specific stuff. This will look very different
        #! when we implement our own local language model.
        self.client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
        
        self.messages = []


    def message(self, message: str):
        """
        #! This will look very different when we implement our own local language model.
        This function sends a message to the LLM and returns the response.

        Args:
            message (str): The message to send to the LLM

        Returns:
            str: The response from the LLM
        """
        self.messages.append({"role": "user", "content": message}) #TODO: Implement some kind of chatlog system

        completion = self.client.complete(
            model = self.model,
            messages = self.messages,
        )

        return str(completion.choices[0].message)

    def train(self, system_message: str = "You are a helpful assistant."):
        """
        #! This will look very different when we implement our own local language model.
        This function begins the training of the LLM. It retrieves the training data from the 
        database and trains the model. 

        Args:
            system_message (str): The message that initializes the personality of the LLM

        """

        db = dbm.DBManager()

        messages = [{"role": "system", "content": system_message},]
        training_data = db.getTrainingData(self.name)

        for data in training_data:
            messages.append({"role": "user", "content": data[0]})
            messages.append({"role": "assistant", "content": data[1]})
        

        self.status = "Trained"

    def check_status(self):
        return self.status
