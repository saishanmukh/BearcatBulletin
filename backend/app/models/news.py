from app.db import db

class News(db.Model):
    __table__name = 'news'

    news_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    headline = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    hashtag = db.Column(db.String(80), nullable=True)
    posted_by = db.Column(db.String(80), nullable=False)
    channel = db.Column(db.String(120), nullable=True)
    start_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    end_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __init__(self, headline, description, category, hashtag, posted_by, channel, start_date, end_date):
        self.headline = headline
        self.description = description
        self.category = category
        self.hashtag = hashtag
        self.posted_by = posted_by
        self.channel = channel
        self.start_date = start_date
        self.end_date = end_date

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
            'start_date': self.start_date,
            'end_date': self.end_date
        }      