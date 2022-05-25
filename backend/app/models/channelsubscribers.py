from app.db import db

class ChannelSubscribers(db.Model):
    __table__name = 'channel_subscribers'

channelsubscribers_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
channel_id = db.Column(db.Integer, db.ForeignKey('channel.channel_id'), nullable=False)
id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

def __init__(self, channel_id, id):
    self.channel_id = channel_id
    self.id = id

def __repr__(self) -> str:
    return f'<ChannelSubscribers id={self.channelsubscribers_id}>'

def json(self) -> dict:
    return {
    'channelsubscribers_id': self.channelsubscribers_id,
    'channel_id': self.channel_id,
    'id': self.id
    }
