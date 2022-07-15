""" Main Method Docstring Template """
from flask import Flask

application = Flask(__name__)


@application.route('/')
def hello_world():
    """ Hello World Docstring Template """
    return 'Hola Mundo'


if __name__ == '__main__':
    application.run()
