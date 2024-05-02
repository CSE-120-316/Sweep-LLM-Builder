# AJ Grant
# 2024-05-01
# ChatBot.py
# Communicates with the LLM_Code and DBManager to finetune and interact with the LLM.

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
        # Check if the dataset exists
        if not dbm.checkDataset(data_set):
            return "Dataset not found."

        # Set data location "~/app/llm-datasets/..." DONT ADD THE .json
        datalocation = key.datasets_location + data_set


        # Train the model
        self.trainer = LLamaTrainer.LlamaTrainer(self.name, datalocation, self.model)
        self.trainer.trainLLM()
        
        self.status = "Trained"

    def message(self, message: str):
        """
        This function sends a message to the LLM and returns the response.

        Args:
            message (str): The message to send to the LLM

        Returns:
            str: The response from the LLM
        """

        pass


    def check_status(self):
        return self.status