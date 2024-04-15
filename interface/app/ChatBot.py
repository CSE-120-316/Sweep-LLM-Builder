import app.DBManager as dbm
import sys
import app.LLM_Code.LlamaTrainer as LLamaTrainer
import app.LLM_Code.LlamaChatBot as LLamaChatBot
import app.key as key

import os

class ChatBot:
    def __init__(self, name: str, model: str):
        self.name = name
        self.model = model
        self.status = "Untrained"

        self.trainer = None
        self.client = None
        
    def train(self, data_set: str):
        """
        #! This will look very different when we implement our own local language model.
        This function begins the training of the LLM. It retrieves the training data from the 
        database and trains the model. 

        Args:
            data_set (str): The name of the dataset to train the LLM

        """

        db = dbm.DBManager()

        # Check if dataset exists in Postgres database
        if not db.checkDataset(data_set):
            return "Dataset does not exist"
        
        # Prepare the training data
        datalocation = db.prepDataset(data_set)

        # Train the model
        self.trainer = LLamaTrainer.LlamaTrainer(self.model, datalocation, 2e-4)
        self.trainer.trainLLM()
        
        self.status = "Trained"

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

        completion = self.client.chat.completions.create(
            model = self.model,
            messages = self.messages,
        )

        return str(completion.choices[0].message)


    def check_status(self):
        return self.status