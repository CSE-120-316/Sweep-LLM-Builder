# Ashley Gonzalez Perez May 8, 2024

from flask import Flask, request, render_template, redirect, session
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def pick():
    return render_template('chat.html')

@app.route('/fine_tune')
def process():
    return render_template('fine_tune.html')

if __name__ == '__main__':
    app.run(debug=True, port=5050)
