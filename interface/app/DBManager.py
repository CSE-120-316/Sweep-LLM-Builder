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

    def addDocument(self, LLMname: str, question: str, answer: str):
        """
        This function receives the training data for the LLM.
        
        Args:
            LLMname (str): The name of the LLM
            title (str): The title of the document
            text (str): The contents of the document
            
        Returns:
        str: A message indicating the success or failure of the operation
        """

        # Check if the table already exists
        self.cur.execute(f"SELECT to_regclass('{LLMname}')")
        if not self.cur.fetchone()[0]:
            # If not, create a new table
            self.cur.execute(f"CREATE TABLE {LLMname} (id SERIAL, question TEXT, answer TEXT)")
            print(f"Table {LLMname} not found, creating new table.")
        # Save the training data to the table
        self.cur.execute(f"INSERT INTO {LLMname} (question, answer) VALUES (%s, %s)", (question, answer))
        self.conn.commit()
        self.cur.close()
    
    def getTrainingData(self, LLMname: str, start = None, end = None):
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
            self.cur.execute(f"SELECT * FROM {LLMname}")
        else:
            self.cur.execute(f"SELECT * FROM {LLMname} LIMIT {end} OFFSET {start}")
        data = self.cur.fetchall()
        self.cur.close()
        return data

    def deleteEntry(self, LLMname: str, title: str): #TODO
        """
        This function deletes a document from the training data.
        
        Args:
            LLMname (str): The name of the LLM
            title (str): The title of the document to delete
            
        Returns:
            str: A message indicating the success or failure of the operation
        """
        pass

    def deleteLLMTable(self, LLMname: str): #TODO
        """
        This function deletes the table associated with the LLM.
        
        Args:
            LLMname (str): The name of the LLM
            
        Returns:
            str: A message indicating the success or failure of the operation
        """
        pass