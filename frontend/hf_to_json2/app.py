# import pandas as pd

# #reading the file
# parquet_file_path = 'example.parquet'  # Replace with the path to your Parquet file
# df = pd.read_parquet(parquet_file_path)

# #Convertion DataFrame to JSON
# json_data = df.to_json(orient='records')

# # Saving the JSON to File
# json_file_path = 'finish/output.json'  # Path to save the JSON file in the 'finish' folder
# with open(json_file_path, ik6ry7h mv'w') as json_file:
#     json_file.write(json_data)

# print(f"JSON file saved: {json_file_path}")

# from flask import Flask, request, render_template
# import pandas as pd
# import os

# app = Flask(__name__)

# UPLOAD_FOLDER = 'uploads'
# FINISH_FOLDER = 'finish'
# ALLOWED_EXTENSIONS = {'parquet'}

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['FINISH_FOLDER'] = FINISH_FOLDER

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return 'No file part'
#     file = request.files['file']
#     if file.filename == '':
#         return 'No selected file'
#     if file and allowed_file(file.filename):
#         filename = file.filename
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        
#         parquet_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         df = pd.read_parquet(parquet_file_path)

        
#         json_data = df.to_json(orient='records')

        
#         json_filename = filename.split('.')[0] + '.json'
#         json_file_path = os.path.join(app.config['FINISH_FOLDER'], json_filename)
#         with open(json_file_path, 'w') as json_file:
#             json_file.write(json_data)

#         #return f'JSON file saved: {json_file_path}'
#         return render_template('finetuning.html')
#     else:
#         return 'Invalid file format'

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, request, render_template, redirect, url_for, session
# import pandas as pd
# import os

# app = Flask(__name__)

# UPLOAD_FOLDER = 'uploads'
# FINISH_FOLDER = 'finish'
# ALLOWED_EXTENSIONS = {'parquet'}
# SECRET_KEY = 'your_secret_key_here'  # Change this to a random string

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['FINISH_FOLDER'] = FINISH_FOLDER
# app.config['SECRET_KEY'] = SECRET_KEY

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/')
# def index():
#     if 'username' in session:
#         return render_template('index.html')
#     return redirect(url_for('login'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         # Check if username and password are correct (you need to implement this)
#         # If correct, set the session username and redirect to index
#         session['username'] = request.form['username']
#         return redirect(url_for('index.html'))
#     return render_template('intro.html')

# @app.route('/register', methods=['POST'])
# def register():
#     # Implement registration logic here (you need to implement this)
#     # After successful registration, redirect to login page
#     return redirect(url_for('login'))

# @app.route('/logout')
# def logout():
#     # Clear the session and redirect to login page
#     session.pop('username', None)
#     return redirect(url_for('login'))

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'username' not in session:
#         return redirect(url_for('login'))
    
#     if 'file' not in request.files:
#         return 'No file part'
#     file = request.files['file']
#     if file.filename == '':
#         return 'No selected file'
#     if file and allowed_file(file.filename):
#         filename = file.filename
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
#         parquet_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         df = pd.read_parquet(parquet_file_path)
        
#         json_data = df.to_json(orient='records')
        
#         json_filename = filename.split('.')[0] + '.json'
#         json_file_path = os.path.join(app.config['FINISH_FOLDER'], json_filename)
#         with open(json_file_path, 'w') as json_file:
#             json_file.write(json_data)

#         #return f'JSON file saved: {json_file_path}'
#         return render_template('finetuning.html')
#     else:
#         return 'Invalid file format'

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, request, render_template, redirect, session
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
#     username = request.form['username']
#     if username in users:
#         return 'User already exists'
#     else:
#         password = request.form['password']
#         users[username] = {'password': password}
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
#             return render_template('index.html')
#         else:
#             return 'Invalid file format'
#     return render_template('index.html')

# @app.route('/create_account')
# def create_account():
#     return render_template('create_account.html')

# if __name__ == '__main__':
#     app.run(debug=True)





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
#     # Registration logic
#     pass

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

#             return render_template('index.html')
#         else:
#             return 'Invalid file format'
#     return render_template('index.html')

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
        return redirect('/upload')
    return render_template('intro.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username]['password'] == password:
        session['username'] = username
        return redirect('/upload')
    else:
        return 'Invalid username or password'

@app.route('/register', methods=['POST'])
def register():
    # Registration logic
    pass

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if 'username' not in session:
        return redirect('/')
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            parquet_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            json_filename = filename.split('.')[0] + '.json'
            json_file_path = os.path.join(app.config['FINISH_FOLDER'], json_filename)
            
            convert_to_json(parquet_file_path, json_file_path)

            return render_template('finetuning.html')
        else:
            return 'Invalid file format'
    return render_template('index.html')

@app.route('/create_account')
def create_account():
    return render_template('create_account.html')

if __name__ == '__main__':
    app.run(debug=True)
