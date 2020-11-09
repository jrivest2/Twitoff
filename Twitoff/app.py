"""Main app/routing file for Twitoff"""

from flask import Flask

def create_app():
    app = Flask(__name__)

    #TODO - Make rest of application
    @app.route('/')
    def root():
        return "Hello, Twitoff"
    return app

