from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

# Initializing Flask Extensions
bootstrap = Bootstrap()


def create_app(config_name):
    # Initializing application
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Intializing flask extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Setting config
    from .request import configure_request
    configure_request(app)

    # Will add the view and forms

    return app
# Setting up configurations
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')

# from app import views
# from app import error
