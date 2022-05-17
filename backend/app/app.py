from flask import Flask, redirect, url_for, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from apifairy import APIFairy
from dotenv import load_dotenv

from app.config import DevelopmentConfig
import os

from app.ma import ma
from app.db import db


# from resources.user import User, Users, user_ns, users_ns
from marshmallow import ValidationError

from sqlalchemy.exc import IntegrityError


migrate = Migrate(compare_type=True)
cors = CORS()
apifairy = APIFairy()
load_dotenv()


def create_app(config_class=DevelopmentConfig):
    from app.models import user
    app = Flask(__name__)
    
    # Configure the app from config file
    app.config.from_object(config_class)

    # Initialize the db
    db.init_app(app)

    # linking migrations to the app
    migrate.init_app(app, db)

    # linking marshmallow to the
    ma.init_app(app)

    # enable CORS
    CORS(app)

    # linking apifairy to the app (for documentation)
    apifairy.init_app(app)

    # register blueprints
    from app.resources.user import users




    app.register_blueprint(users, url_prefix='/api')

    
    @app.errorhandler(Exception)
    def handle_error(e):
        if isinstance(e, ValidationError):
            return jsonify({"error":e.messages}), 400

        elif isinstance(e, IntegrityError):
            errorInfo = e.orig.args
            return jsonify({"error": errorInfo[1]}), 400
        return jsonify(e.args), 500

    return app

