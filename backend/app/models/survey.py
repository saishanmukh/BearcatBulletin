from app.db import db

class Survey(db.Model):
    __table__name = 'survey'

    survey_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    survey_name = db.Column(db.String(80), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    end_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    category = db.Column(db.String(120), nullable=False)

    # create relation with survey_parties table
    survey_parties = db.relationship('SurveyParties', backref='survey', lazy=True)

    # create relation with survey table
    survey_responses = db.relationship('SurveyResponses', backref='survey', lazy=True)

    def __init__(self, name, start_date, end_date, category):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.category = category    

    def __repr__(self) -> str:
        return f'<Survey survey_id={self.survey_id}>'

    def json(self) -> dict:
        return {
            'survey_id': self.survey_id,
            'survey_name': self.survey_name,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'category': self.category
        }