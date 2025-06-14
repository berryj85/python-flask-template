from flask import Flask

from src.controller import service_information


def create_app():
    app = Flask(__name__)
    app.config.from_envvar("CONFIGURATION_FILE", silent=True)
    app.register_blueprint(service_information.blueprint)
    return app
