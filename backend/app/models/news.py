from app.db import db

class News(db.Model):
    __table__name = 'news'

    news_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    headline = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    hashtag = db.Column(db.String(80), nullable=True)
    posted_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    channel = db.Column(db.String(120), nullable=True)
    posted_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    edited_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    # create a relation with user_news table
    user_news = db.relationship('UserNews', backref='news', lazy=True)

    # create a relation with images table
    images = db.relationship('Images', backref='news', lazy=True)

    def __init__(self, headline, description, category, hashtag, posted_by, channel, posted_date, edited_date):
        self.headline = headline
        self.description = description
        self.category = category
        self.hashtag = hashtag
        self.posted_by = posted_by
        self.channel = channel
        self.posted_date = posted_date
        self.edited_date = edited_date

    def __repr__(self) -> str:
        return f'<News id={self.news_id}>'

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