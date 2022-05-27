from app.db import db
from sqlalchemy import Enum
import enum

class RolesEnum(enum.Enum):
    USER = "USER"
    ADMIN = "ADMIN"

class User(db.Model):
    __table__name = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(Enum(RolesEnum), default=RolesEnum.USER)
    created_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    password = db.Column(db.String(80), nullable=False)

    # create relation with news
    news = db.relationship('News', backref='user', lazy=True)

    # create relation with user_news
    user_news = db.relationship('UserNews', backref='user', lazy=True)

    # create relation with channel
    channel = db.relationship('Channel', backref='user', lazy=True)

    # create relation with channel_subscriptions
    channel_subscriptions = db.relationship('ChannelSubscriptions', backref='user', lazy=True)

    # create relation with survey_responses
    survey_responses = db.relationship('SurveyResponses', backref='user', lazy=True)


    def __init__(self, first_name, last_name, email, password, role):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role = role

    
    def __repr__(self) -> str:
        return f'<User id={self.id} email={self.email} >'

    def json(self) -> dict:
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'role': self.role,
            'created_date': self.created_date
        }

    @classmethod
    def find_by_email(cls, email: str) -> 'User':
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id: int) -> 'User':
        return cls.query.filter_by(id=_id).first()

    def update(self, data: dict) -> None:
        for key, value in data.items():
            setattr(self, key, value)
        db.session.commit()

    # def update(cls, _id: int, data: dict) -> 'User':
    #     user = cls.find_by_id(_id)
    #     if not user:
    #         return None
    #     for key, value in data.items():
    #         setattr(user, key, value)
    #     user.save_to_db()
    #     return user

    # @classmethod
    # def check_password(cls, user: 'User', password: str) -> bool:
    #     return user.password == password

    def check_password(self, password: str) -> bool:
        return self.password == password

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
