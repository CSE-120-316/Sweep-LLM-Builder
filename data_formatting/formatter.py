import json
import os

def get_files(db_name, usr, psswd, host, port):
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

  # Assuming a specific format for the .json files similar to what one would expect from the SQuAD (Stanford Question and Answer) data set we can concatenate the files as follows:
  for filename in json_files:
        with open(filename, 'r') as file:
            data = json.load(file)
            for article in data['data']:
                for paragraph in article['paragraphs']:
                    context = paragraph['context']
                    for qa in paragraph['qas']:
                        question = qa['question']
                        for answer in qa['answers']:
                            rows.append({
                                'Context (Paragraph)': context,
                                'Question': question,
                                'Answer Text': answer['text'],
                                'Answer Start Position': answer['answer_start']
                            })

  # Close connection to DB
  conn.close()

  # Return list
  return json_files

def join_files(json_list):
  """
  This function takes in a list of previously joined json objects and combines into a single .json file
  """

  # Empty list to keep python objects
  python_objs = []

  # Load each .json file into pyton obj
  for jsonfile in json_list:
    with open(jsonfile, 'r') as f:
      python_objs.append(json.load(f))

  # Dump objects into a json file
  with open("combined_data.json", 'w') as f:
    json.dump(python_objs, f, indent=4)


# No longer need function to streamline process for converting .json files to apache parquet. This is because
# in the finetuning code when we read from .json we will already convert to parquet automatically.