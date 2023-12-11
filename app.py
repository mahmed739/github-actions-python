"""
This is a simple Python web application using Flask.

It serves a "Hello, World!" message when accessed in a web browser.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    Route handler for the root URL.

    This function handles incoming HTTP GET requests to the root URL ("/").
    It returns a "Hello, World!" message.
    """
    return 'Hello, World From Integrant!'
    #TODO: important

if __name__ == '__main__':
    app.run()
