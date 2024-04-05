import psycopg2
import pandas as pd
import json
import pyarrow as pa
import pyarrow.parquet as pq
from pyarrow import json

def formatter(db_name, usr, psswd, host, port):
  """
  This function interacts with the provided postgres database in order to retrieve the .json files
  that are being stored in its table. These .json files are then loaded into a list.
  """

  # Connect to DB
  conn = psycopg2.connect(db_name=db_name, user=usr, password=psswd, host=host, port=port)
  
  cursor = conn.cursor()

  # SQL query to get the .json files
  query = "Retrieve json_files"

  cursor.execute(query)

  # Retrieve info from query
  rows = cursor.fetchall()

  # Empty list to store .json files
  json_files = []

  # Append to list
  for row in rows:
    json_files.append(json.loads(row[0]))

  # Close connection to DB
  conn.close()

  # Return list
  return json_files
