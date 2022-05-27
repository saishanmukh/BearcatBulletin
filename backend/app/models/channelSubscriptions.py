from app.db import db

class ChannelSubscriptions(db.Model):
    __table__name = 'channel_subscriptions'

    subscription_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    subscribed_channel_id = db.Column(db.Integer, db.ForeignKey('channel.channel_id'), nullable=False)
    subscriber_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, subscribed_channel_id, subscriber_user_id):
        self.subscribed_channel_id = subscribed_channel_id
        self.subscriber_user_id = subscriber_user_id

    def __repr__(self) -> str:
        return f'<ChannelSubscribers id={self.subscription_id}>'

    def json(self) -> dict:
        return {
        'subscription_id': self.subscription_id,
        'subscribed_channel_id': self.subscribed_channel_id,
        'subscriber_user_id': self.subscriber_user_id
        }
