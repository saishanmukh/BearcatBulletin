from distutils.log import error
from email import header
from pyexpat import ErrorString
from flask import Blueprint, abort, jsonify, Response, request
from apifairy import body, response, other_responses, arguments
from marshmallow import fields

from app.models.news import News
from app.schemas.news import NewsSchema, NewsSchemaWithImages, NewsSchemaFilterArguments, CreateNewsSchema


from app.models.images import Images
import os

from app.config import basedir


NEWS_NOT_FOUND = "News not found"

news_schema = NewsSchema()
news_schema_for_create = CreateNewsSchema()
news_schema_many = NewsSchema(many=True)


news = Blueprint('news', __name__)


# insert new news
@news.route('/news', methods=['POST'])
@response(news_schema)
@other_responses({404: 'User not found.'})
def create_news():
    """Create a news"""
    request_data = request.form
    request_files = request.files
    errors = news_schema_for_create.validate(request_data)
    print(request_data)
    print(errors)
    if errors:
        return abort(Response(f'Missing {(", ").join(list(errors.keys()))}', status=400))

    else:
        if len(request_files) == 0:
            return jsonify({'code': 400, 'messages': ['images are required']}), 400
        # load the data
        data = news_schema_for_create.load(request_data)
        # create the news
        news = News(**data)
        # # save the news
        news.save_to_db()

        image_folder = f'{basedir}\static\images\{news.news_id}'
        # save the images
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
        
        for i, image in enumerate(request_files):
            image_data = request_files[image]
            # check if the directory exists
            image_data.save(f'{image_folder}/{i+1}.jpg')
            image_data.close()

            # save to images table
            image = Images(news_id=news.news_id, image_path=f'{news.news_id}/{i+1}.jpg')
            image.save_to_db()

        return news

# retrieve a news by id
@news.route('/news/<int:id>', methods=['GET'])
@response(news_schema, 200)
@other_responses({404: 'News not found.'})
def get_by_id(id):
    """Retrieve a news by id"""
    news = News.find_by_id(id)
    if news:
        return news
    else:
        abort(404, NEWS_NOT_FOUND)

# get all news
@news.route('/news', methods=['GET'])
@response(news_schema_many)
@arguments(NewsSchemaFilterArguments)
def get_all(filter_args):
    """Retrieve all news"""
    news = News.find_all_news()
    return news