from app.db import db

class TelecastedNews(db.Model):
    __table__name = 'telecasted_news'

telecastednews_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
news_id = db.Column(db.Integer, db.ForeignKey('news.news_id'), nullable=False)
channel_id = db.Column(db.Integer, db.ForeignKey('channel.channel_id'), nullable=False)

def __init__(self, news_id, channel_id):
    self.news_id = news_id
    self.channel_id = channel_id

def __repr__(self) -> str:
    return f'<TelecastedNews id={self.telecastednews_id}>'

def json(self) -> dict:
    return {
    'telecastednews_id': self.telecastednews_id,
    'news_id': self.news_id,
    'channel_id': self.channel_id
    }