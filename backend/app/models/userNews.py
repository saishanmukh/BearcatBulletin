from app.db import db

class UserNews(db.Model):
    __table__name = 'user_news'

    user_news_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    news_id = db.Column(db.Integer, db.ForeignKey('news.news_id'), nullable=False)
    is_saved = db.Column(db.Boolean, nullable=False, default=False)
    is_liked = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, user_id, news_id, is_saved, is_liked):
        self.user_id = user_id
        self.news_id = news_id
        self.is_saved = is_saved
        self.is_liked = is_liked

    def __repr__(self) -> str:
        return f'<UserNews id={self.user_news_id}>'

    def json(self) -> dict:
        return {
            'user_news_id': self.user_news_id,
            'user_id': self.user_id,
            'news_id': self.news_id,
            'is_saved': self.is_saved,
            'is_liked': self.is_liked
        }