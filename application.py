""" Main Method Docstring Template """
from flask import Flask, render_template

application = Flask(__name__)


@application.route('/')
def hello_world():
    """ Hello World Docstring Template """
    return render_template('index.html')


if __name__ == '__main__':
    application.run()
