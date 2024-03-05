import pickle

class LM:
    def __init__(self, name: str, model: str):
        self.name = name
        self.model = model
        self.training_data = None
        self.status = "Untrained"

    def message():
        pass

    def train():
        pass

    def check_status(name: str):
        # Get the LLm from pickle file and return its status
        with open(f"llms/{name}.pkl", "rb") as f:
            llm = pickle.load(f)
        return llm.status
