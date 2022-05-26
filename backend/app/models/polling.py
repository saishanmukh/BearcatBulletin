from app.db import db

class Polling(db.Model):
    __table__name = 'polling'

    polling_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    end_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    category = db.Column(db.String(120), nullable=False)

    # create relation with user
    user = db.relationship('User', backref='polling', lazy=True)

    # create relation with results
    results = db.relationship('Results', backref='polling', lazy=True)

    def __init__(self, name, start_date, end_date, category):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.category = category    

    def __repr__(self) -> str:
        return f'<Polling id={self.polling_id}>'

    def json(self) -> dict:
        return {
            'polling_id': self.polling_id,
            'name': self.name,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'category': self.category
        }