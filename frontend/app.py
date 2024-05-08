
# from flask import Flask, request, render_template, redirect, session
# import pandas as pd
# import os

# app = Flask(__name__)
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# UPLOAD_FOLDER = 'uploads'
# FINISH_FOLDER = 'finish'
# ALLOWED_EXTENSIONS = {'parquet'}

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['FINISH_FOLDER'] = FINISH_FOLDER

# # Simulated database for users
# users = {
#     'user1@example.com': {'password': 'password123', 'name': 'User1'},
#     # Add more users as needed
# }

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# def convert_to_json(parquet_file_path, json_file_path):
#     df = pd.read_parquet(parquet_file_path)
#     json_data = df.to_json(orient='records')
#     with open(json_file_path, 'w') as json_file:
#         json_file.write(json_data)

# @app.route('/')
# def index():
#     if 'username' in session:
#         return redirect('/upload')
#     return render_template('intro.html')

# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form['username']
#     password = request.form['password']
#     if username in users and users[username]['password'] == password:
#         session['username'] = username
#         return redirect('/upload')
#     else:
#         return 'Invalid username or password'

# @app.route('/register', methods=['POST'])
# def register():
#     if request.method == 'POST':
#         name = request.form['name']
#         lastname = request.form['lastname']
#         username = request.form['username']
#         password = request.form['password']
#         password2 = request.form['password2']

#         # You can add your registration logic here
#         # For simplicity, let's just store the user in the 'users' dictionary
#         users[username] = {'password': password, 'name': name, 'lastname': lastname}

#         # Redirect to the login page after successful registration
#         return redirect('/')

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if 'username' not in session:
#         return redirect('/')
#     if request.method == 'POST':
#         file = request.files['file']
#         if file.filename == '':
#             return 'No selected file'
#         if file and allowed_file(file.filename):
#             filename = file.filename
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
#             parquet_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             json_filename = filename.split('.')[0] + '.json'
#             json_file_path = os.path.join(app.config['FINISH_FOLDER'], json_filename)
            
#             convert_to_json(parquet_file_path, json_file_path)

#             return render_template('finetuning.html')
#         else:
#             return 'Invalid file format'
#     # return render_template('index.html')
#     # return render_template('process.html')
#      return render_template('choose.html')

# @app.route('/create_account')
# def create_account():
#     return render_template('create_account.html')

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, render_template, redirect, session
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

UPLOAD_FOLDER = 'uploads'
FINISH_FOLDER = 'finish'
ALLOWED_EXTENSIONS = {'parquet'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['FINISH_FOLDER'] = FINISH_FOLDER

# Simulated database for users
users = {
    'user1@example.com': {'password': 'password123', 'name': 'User1'},
    # Add more users as needed
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_to_json(parquet_file_path, json_file_path):
    df = pd.read_parquet(parquet_file_path)
    json_data = df.to_json(orient='records')
    with open(json_file_path, 'w') as json_file:
        json_file.write(json_data)

@app.route('/')
def index():
    if 'username' in session:
        return redirect('/pick')
    return render_template('intro.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username]['password'] == password:
        session['username'] = username
        return redirect('/pick')
    else:
        return 'Invalid username or password'

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']

        # You can add your registration logic here
        # For simplicity, let's just store the user in the 'users' dictionary
        users[username] = {'password': password, 'name': name, 'lastname': lastname}

        # Redirect to the login page after successful registration
        return redirect('/')

@app.route('/pick')
def pick():
    if 'username' not in session:
        return redirect('/')
    return render_template('choose.html')

@app.route('/create_account')
def create_account():
    return render_template('create_account.html')

@app.route('process')
def process():
    return render_template('process.html')

if __name__ == '__main__':
    app.run(debug=True)
