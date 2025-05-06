import os

from flask import Flask

def create_app():
    #TODO: Add test_config as a parameter

    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # TODO: Add database path later
    )

    app.config.from_pyfile('config.py', silent=True)
    # TODO: Add test_config

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return '<h1>Welcome to the Movie Tracker!</h1>'
    
    return app