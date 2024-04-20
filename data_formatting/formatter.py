import json
import os
import psycopg2

# Defining new functions to take the place of the ones below. No longer going to be using postgres sql and instead will be storing and retrieving data from docker volume

def load_format(file_path):
  """
  This function loads a JSON file and makes sure it reads.
  """
  with open(file_path, 'r', encoding='utf-8') as file:
     data = json.load(file)
  
  return data

def combine_json_files(input_dir):
  """
  This functions combines JSON files from a given directory.
  """
  combined_data = [] # Empty list to store JSON files

  for filename in os.listdir(input):
    if filename.endswith('.json'):
      file_path = os.path.join(input_dir, filename)
      combined_data.extend(load_format(file_path))

  return combined_data

def save_combined_dataset(output_file, dataset):
  """
  Save the combined dataset as a JSON file.
  """ 
  with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(dataset, file, ensure_ascii=False, indent=2)