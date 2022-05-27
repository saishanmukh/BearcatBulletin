from app.db import db

class SurveyResponses(db.Model):
    __table__name = 'survey_responses'

    response_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.survey_id'), nullable=False)
    responsed_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    responsed_to = db.Column(db.Integer, nullable=False , autoincrement=True)

    def __init__(self, survey_id, responsed_user_id, responsed_to):
        self.survey_id = survey_id
        self.responsed_user_id = responsed_user_id
        self.responsed_to = responsed_to

    def __repr__(self) -> str:
        return f'<Reponse response_id={self.response_id}>'

    def json(self) -> dict:
        return {
            'response_id': self.response_id,
            'survey_id': self.survey_id,
            'responsed_user_id': self.responsed_user_id,
            'responsed_to': self.responsed_to
        }