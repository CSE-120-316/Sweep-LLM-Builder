import psycopg2
import json
import os
import app.key as key

class DBManager:
    def __init__(self):
        self.conn = psycopg2.connect( #TODO We can not initialize authentication here, we need to take it in.
            dbname="mydb",
            user="UCMStudents6",
            password="KRKT86V9wr8tkGHkQN6tM8mHDmk2R7",
            host=key.database_host,
            port="5432"
        )
        self.cur = self.conn.cursor()

    def addDocument(self, dataName: str, dataContent: str):
        """
        This function receives the training data for the LLM.
        
        Args:
            dataName (str): The name of the LLM
            dataContent (dict): The training data to save to the database

        Returns:
            str: A message indicating the success or failure of the operation
        """

        # Check if the table already exists
        self.cur.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{dataName}')")
        if self.cur.fetchone()[0] == False:
            # Create a new table with the name dataName
            self.cur.execute(f"CREATE TABLE {dataName} (id SERIAL PRIMARY KEY, document TEXT)")
            self.conn.commit()

        # Insert the dataContent as an entry in the table
        self.cur.execute(f"INSERT INTO {dataName} (document) VALUES ('{dataContent}')")
        self.conn.commit()

        self.cur.close()
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
                
        if index == "all":  # Delete all entries
            self.cur.execute(f"DELETE FROM {LLMname}") # Delete all entries
        else:
            self.cur.execute(f"DELETE FROM {LLMname} WHERE id = {index}")
        self.conn.commit()
        self.cur.close()
        return "Entry deleted"  

    def deleteLLMTable(self, LLMname: str): #TODO
        """
        This function deletes the table associated with the LLM.
        
        Args:
            LLMname (str): The name of the LLM
            
        Returns:
            str: A message indicating the success or failure of the operation
        """
        self.cur.execute(f"DROP TABLE {LLMname}")
        self.conn.commit()
        self.cur.close()
        return "Table deleted"
    
    def checkDataset(self, dataName: str):
        """
        This function checks if a dataset exists in the database.

        Args:
            dataName (str): The name of the dataset

        Returns:
            bool: True if the dataset exists, False otherwise
        """
        self.cur.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{dataName}')")
        return self.cur.fetchone()[0]
    
    def prepDataset(self, dataName: str):
        """
        This function prepares the dataset by placing it in a .json file.

        Args:
            dataName (str): The name of the dataset

        Returns:
            str: A message indicating the success or failure of the operation
        """
        # Create the .json file. It takes each entry from the table and places it as
        # a new line in the .json file.
        self.cur.execute(f"SELECT * FROM {dataName}")
        data = self.cur.fetchall()
        with open(key.datasets_location + dataName + ".json", "w") as f:
            for entry in data:
                f.write(entry[1] + "\n")
        self.cur.close()
        f.close()

        return f"{key.datasets_location}{dataName}.json"