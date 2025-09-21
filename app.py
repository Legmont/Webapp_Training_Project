from flask import Flask
from python_files.routes.home import homepage_bp
from python_files.routes.about import about_bp
from dotenv import load_dotenv
import os

import pkgutil
import importlib


def create_app():
    app = Flask(__name__)
    SECRET_KEY= os.getenv("SECRET_KEY")
    print(SECRET_KEY)
    # Configure the database
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meal_planner.db'
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #set bs secret key
    #app.secret_key ="H"
    # Initialize extensions
    #db.init_app(app)
    #migrate.init_app(app, db)

    # Register Blueprints

    app.register_blueprint(homepage_bp)
    app.register_blueprint(about_bp)


    return app