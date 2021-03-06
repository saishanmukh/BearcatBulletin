from app.db import db

class Channel(db.Model):
    __table__name = 'channel'

    channel_id = db.Column(db.Integer, primary_key=True, autoincrement=True)    
    channel_name = db.Column(db.String(80), nullable=False)  
    admin_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # create a relation with channel_subscriptions table
    channel_subscriptions = db.relationship('ChannelSubscriptions', backref='channel', lazy=True)
    
    # create a realtion with the news table
    news = db.relationship('News', backref='channel', lazy=True)

    def __init__(self, channel_name, admin_user_id):
        self.channel_name = channel_name
        self.admin_user_id = admin_user_id

    def __repr__(self) -> str:
        return f'<Channel channel_id={self.channel_id}>'

    def json(self) -> dict:
        return {
            'channel_id': self.channel_id,
            'channel_name': self.channel_name,
            'admin_user_id': self.admin_user_id
        }

    @classmethod
    def find_by_id(cls, channel_id: int) -> 'Channel':
        return cls.query.filter_by(channel_id=channel_id).first()

    @classmethod
    def find_all_channels(cls) -> list:
        return cls.query.all()
    
    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
