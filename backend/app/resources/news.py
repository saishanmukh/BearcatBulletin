from flask import Blueprint, abort, jsonify, Response
from apifairy import body, response, other_responses, arguments


from app.models.news import News
from app.schemas.news import NewsSchema, NewsSchemaWithImages

NEWS_NOT_FOUND = "News not found"

news_schema = NewsSchema()
news_schema_many = NewsSchema(many=True)


news = Blueprint('news', __name__)


# insert new news
@news.route('/news', methods=['POST'])
@body(NewsSchemaWithImages)
@response(news_schema, 201)
def create_news(news):
    """Create a news"""
    news = News(**news)
    news.save_to_db()
    return news, 201

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
@response(NewsSchemaWithImages, 200)
def get_all():
    """Retrieve all news"""
    news = News.find_all_news()
    return news