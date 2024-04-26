from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
import json

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# def convert_to_json(file_path):
#     # Your logic to convert the file to JSON goes here
#     # For example, if you're using Hugging Face transformers, you can use their functionality to convert to JSON
#     # Here's a dummy example:
#     data = {"file_path": file_path}
#     return json.dumps(data)
def convert_to_json(file_path):
    from transformers import AutoTokenizer, AutoModelForSequenceClassification

    # Load the Hugging Face model and tokenizer
    model_name = "bert-base-uncased"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    # Read the input file
    with open(file_path, 'r') as file:
        text = file.read()

    # Tokenize the text
    inputs = tokenizer(text, truncation=True, padding=True, return_tensors="pt")

    # Perform inference
    outputs = model(**inputs)

    # Convert the output to JSON
    result = {
        "file_path": file_path,
        "input_text": text,
        "predictions": outputs.logits.tolist()
    }

    return json.dumps(result)

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
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        # Convert the file to JSON
        json_data = convert_to_json(file_path)
        return json_data

if __name__ == '__main__':
    app.run(debug=True)
