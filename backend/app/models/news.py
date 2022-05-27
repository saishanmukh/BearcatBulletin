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
    edited_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    # create a relation with user_news table
    user_news = db.relationship('UserNews', backref='news', lazy=True)

    # create a relation with images table
    images = db.relationship('Images', backref='news', lazy=True)

    # create a relation with channel table
    # channel = db.relationship('Channel', backref='news', lazy=True)

    # # create a relation with telecastednews table
    # telecasted_news = db.relationship('TelecastedNews', backref='news', lazy=True)

    def __init__(self, headline, description, category, hashtag, posted_by, channel, posted_date, edited_date):
        self.headline = headline
        self.description = description
        self.category = category
        self.hashtag = hashtag
        self.posted_by = posted_by
        self.channel = channel
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
        # join news and images
        news = cls.query.join(Images, News.news_id == Images.news_id).order_by(desc(News.posted_date)).all()
        print(news[0].images)
        return news
            
    
    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()

    # def __repr__(self) -> str:
    #     return f'<News id={self.news_id}>'

    def json(self) -> dict:
        return {
            'news_id': self.news_id,
            'headline': self.headline,
            'description': self.description,
            'category': self.category,
            'hashtag': self.hashtag,
            'posted_by': self.posted_by,
            'channel': self.channel,
            'posted_date': self.posted_date,
            'edited_date': self.edited_date
        }