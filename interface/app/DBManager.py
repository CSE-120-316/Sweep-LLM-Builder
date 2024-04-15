import psycopg2

class DBManager:
    def __init__(self):
        self.conn = psycopg2.connect( #TODO We can not initialize authentication here, we need to take it in.
            dbname="mydb",
            user="user",
            password="pass",
            host="database",
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
        if self.cur.fetchone()[0]:
            return "Table already exists" #TODO Error handling: Maybe throw an error or something.
        
        # Create a table for the LLM
        self.cur.execute(f"CREATE TABLE {dataName} (id SERIAL PRIMARY KEY, document TEXT)")
        self.conn.commit()

        # Insert the training data into the table
        for document in dataContent:
            self.cur.execute(f"INSERT INTO {dataName} (document) VALUES ('{document}')")
        self.conn.commit()

        self.cur.close()
        return "Dataset saved successfully"
    
    def getTrainingData(self, dataName: str, start: int = None, end: int = None):
        """
        This function retrieves the training data for the LLM.
        
        Args:
            LLMname (str): The name of the LLM
            start (int): (Optional) The index of the first document to retrieve
            end (int): (Optional) The index of the last document to retrieve
        
        Returns:
            list: A list of tuples containing the training data
        """

        #TODO Error handling: Table doesn't exist, start > end, end > number of documents, etc.
        # Retrieve the training data from the table, returns a list of tuples
        if start == None and end == None:
            self.cur.execute(f"SELECT * FROM {dataName}")
        else:
            self.cur.execute(f"SELECT * FROM {dataName} WHERE id BETWEEN {start} AND {end}")
        data = self.cur.fetchall()
        self.cur.close()
        return data

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