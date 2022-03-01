from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
import os
from app.views.home import homeblueprint




def regsiterblueprint(app):
    """

    :param app:
    :return:
    """
    app.register_blueprint(homeblueprint)
    return True


def create_app():
    """
    flask app factory function
    :return:
    """
    app = Flask(__name__)

    app.config.from_object('config')
    regsiterblueprint(app)
    return app