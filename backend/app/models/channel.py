from app.db import db

class Channel(db.Model):
    __table__name = 'channel'

    channel_id = db.Column(db.Integer, primary_key=True, autoincrement=True)    
    channel_name = db.Column(db.String(80), nullable=False)  
    admin_id = db.Column(db.Integer, nullable=False)
    subscribers = db.Column(db.String(80), nullable=False)

    # create a relation with channel_subscribers table
    channel_subscribers = db.relationship('ChannelSubscribers', backref='channel', lazy=True)

    # create a relation with user table
    user = db.relationship('User', backref='channel', lazy=True)

    # create a relation with news table
    news = db.relationship('News', backref='channel', lazy=True)

    # create a relation with telecastednews table
    telecasted_news = db.relationship('TelecastedNews', backref='channel', lazy=True)

    def __init__(self, channel_name, admin_id, subscribers):
        self.channel_name = channel_name
        self.admin_id = admin_id
        self.subscribers = subscribers

    def __repr__(self) -> str:
        return f'<Channel id={self.channel_id}>'

    def json(self) -> dict:
        return {
            'channel_id': self.channel_id,
            'channel_name': self.channel_name,
            'admin_id': self.admin_id,
            'subscribers': self.subscribers
        }