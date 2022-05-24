from app.db import db


class Images(db.Model):
    __table__name = 'images'

    image_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    news_id = db.Column(db.Integer, db.ForeignKey('news.news_id'), nullable=False)
    url = db.Column(db.String(80), nullable=False)

    def __init__(self, news_id, url):
        self.news_id = news_id
        self.url = url

    def __repr__(self) -> str:
        return f'<Images id={self.image_id}>'  

    def json(self) -> dict:
        return {
            'image_id': self.image_id,
            'news_id': self.news_id,
            'url': self.url
        }