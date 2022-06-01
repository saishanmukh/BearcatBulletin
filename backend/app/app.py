from email.policy import default
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

from app.models import channelSubscriptions


migrate = Migrate(compare_type=True)
cors = CORS()
apifairy = APIFairy()
load_dotenv()


@apifairy.error_handler
def my_error_handler(status_code, messages):
    return {'code': status_code, 'messages': messages}, status_code

@apifairy.process_apispec
def my_apispec_processor(spec):
    # modify spec as needed here
    print("********************************")
    # spec["paths"]["/api/news"]["post"]['requestBody']['content']['multipart/form-data'] = {'application/json': {'schema': {'$ref': '#/components/schemas/News'}}}
    
    spec["paths"]["/api/news"]["post"] = {'operationId': 'news_create_news', 
    'parameters': [], 'tags': ['News'], 'summary': 'Create a news', 
    'responses': {'200': {'content': {'application/json': {'schema': {'$ref': '#/components/schemas/News'}}}, 'description': 'OK'}}, 
    'requestBody': {'content': {'multipart/form-data': 
    {'schema':     { "type": "object",
    'required': ['headline', 'description', 'posted_by', 'category', 'image'],
    "properties":
          {"headline": {"type": "string"},
            "description" : {"type": "string"},
            "category" : {"type": "string"},
            "hashtag" : {"type": "string"},
            "posted_by" : {"type": "integer"},
            "channel_id" : {"type": "integer"},
            "image": {"type": "string", "format": "binary"}},
        "encoding": {
            "image": {
                "contentType": "image/jpeg",
                }}}
                }
                
                }}}

    # print(spec["paths"]["/api/news"]["post"])

    # { "type": "object",
    # "required": ["id"],
    #     "properties":
    #       {"id": {"type": "string", "format": "uuid"},
    #       "profileImage": {"type": "string", "format": "binary"}},
    #     "encoding": {
    #         "profileImage": {
    #             "contentType": "image/jpeg",
    #             "headers": {
    #                 "Content-Type": "image/jpeg"
    #             }}}}
    # print("********************************")
    return spec

# @APIFairy().process_apispec
# def format_news(spec):
#     return spec
    # print(news)
    # news_schema_many.context["include"] = request.args.getlist("include")
    # return news_schema_many.dump(news)

def create_app(config_class=DevelopmentConfig):
    from app.models import user, news, userNews, channel, images, channelSubscriptions, survey, surveyParties, surveyResponses
    #  birthday, images, polling, 
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
    from app.resources.news import news
    from app.resources.channel import channel




    app.register_blueprint(users, url_prefix='/api')
    app.register_blueprint(news, url_prefix='/api')
    app.register_blueprint(channel, url_prefix='/api')


    
    @app.errorhandler(Exception)
    def handle_error(e):
        if isinstance(e, ValidationError):
            return jsonify({"error":e.messages}), 400

        elif isinstance(e, IntegrityError):
            errorInfo = e.orig.args
            return jsonify({"error": errorInfo[1]}), 400
        return jsonify(e.args), 500

    return app

