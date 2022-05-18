from app.db import db


class Birthday(db.Model):
    __table__name = 'birthday'

    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(80), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    created_by = db.Column(db.String(120), nullable=False)

    def __init__(self, url, created_date, created_by):
        self.url = url
        self.created_date = created_date
        self.created_by = created_by

    def __repr__(self) -> str:
        return f'<Birthday id={self.card_id}>'   

    def json(self) -> dict:
        return {
            'card_id': self.card_id,
            'url': self.url,
            'created_date': self.created_date,
            'created_by': self.created_by
        }