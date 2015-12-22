# from project import user
#
#
# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
from project import app

if __name__ == '__main__':
    app.run()
