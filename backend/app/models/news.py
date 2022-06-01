from app.db import db
from .images import Images
from sqlalchemy import desc

class News(db.Model):
    __table__name = 'news'

    news_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    headline = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    hashtag = db.Column(db.String(80), nullable=True)
    posted_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey('channel.channel_id'),nullable=True)
    posted_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    edited_date = db.Column(db.DateTime, nullable=True)

    # create a relation with user_news table
    user_news = db.relationship('UserNews', backref='news', lazy=True)

    # create a relation with images table
    images = db.relationship('Images', backref='news', lazy=True)


    def __init__(self, headline, description, category,  posted_by, hashtag= None,  channel_id =  None, posted_date = None,  edited_date = None):
        self.headline = headline
        self.description = description
        self.category = category
        self.hashtag = hashtag
        self.posted_by = posted_by
        self.channel_id = channel_id
        self.posted_date = posted_date
        self.edited_date = edited_date

    @classmethod
    def find_by_id(cls, news_id: int) -> 'News':
        return cls.query.filter_by(news_id=news_id).first()

    @classmethod
    def find_all(cls) -> 'News':
        return cls.query.all()

    @classmethod
    def find_all_news(cls):
        news = cls.query.join(Images, News.news_id == Images.news_id).order_by(desc(News.posted_date)).all()
        return news

    @classmethod
    def find_all_news_include(cls, include: list):
        news = cls.query.join(Images, News.news_id == Images.news_id).order_by(desc(News.posted_date)).all()
        return news

        # news = cls.query.join(Images, News.news_id == Images.news_id).order_by(desc(News.posted_date)).all()
        # return news
    
    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

    def __repr__(self) -> str:
        return f'<News news_id={self.news_id}>'

    def json(self) -> dict:
        return {
            'news_id': self.news_id,
            'headline': self.headline,
            'description': self.description,
            'category': self.category,
            'hashtag': self.hashtag,
            'posted_by': self.posted_by,
            'channel_id': self.channel_id,
            'posted_date': self.posted_date,
            'edited_date': self.edited_date
        }