# import pandas as pd

# #reading the file
# parquet_file_path = 'example.parquet'  # Replace with the path to your Parquet file
# df = pd.read_parquet(parquet_file_path)

# #Convertion DataFrame to JSON
# json_data = df.to_json(orient='records')

# # Saving the JSON to File
# json_file_path = 'finish/output.json'  # Path to save the JSON file in the 'finish' folder
# with open(json_file_path, 'w') as json_file:
#     json_file.write(json_data)

# print(f"JSON file saved: {json_file_path}")

from flask import Flask, request, render_template
import pandas as pd
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
FINISH_FOLDER = 'finish'
ALLOWED_EXTENSIONS = {'parquet'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['FINISH_FOLDER'] = FINISH_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        
        parquet_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        df = pd.read_parquet(parquet_file_path)

        
        json_data = df.to_json(orient='records')

        
        json_filename = filename.split('.')[0] + '.json'
        json_file_path = os.path.join(app.config['FINISH_FOLDER'], json_filename)
        with open(json_file_path, 'w') as json_file:
            json_file.write(json_data)

        return f'JSON file saved: {json_file_path}'
    else:
        return 'Invalid file format'

if __name__ == '__main__':
    app.run(debug=True)

