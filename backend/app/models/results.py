from app.db import db

class Results(db.Model):
    __table__name = 'results'

result_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
polling_id = db.Column(db.Integer, db.ForeignKey('polling.polling_id'), nullable=False)
id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
votes = db.Column(db.Integer, nullable=False , autoincrement=True)

def __init__(self, polling_id, id, votes):
    self.polling_id = polling_id
    self.id = id
    self.votes = votes

def __repr__(self) -> str:
    return f'<Results id={self.result_id}>'

def json(self) -> dict:
    return {
        'result_id': self.result_id,
        'polling_id': self.polling_id,
        'id': self.id,
        'votes': self.votes
    }