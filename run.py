from flask import Flask

# Create Flask application instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return 'Hello, World! This is my Flask application.'

# Define a route for a custom endpoint
@app.route('/about')
def about():
    return 'This is the about page of my Flask application.'

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
