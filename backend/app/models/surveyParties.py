from app.db import db

class SurveyParties(db.Model):
    __table__name = 'survey_parties'

    survey_party_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.survey_id'), nullable=False)
    party_name = db.Column(db.String(80), nullable=False)

    def __init__(self, survey_id, party_name):
        self.survey_id = survey_id
        self.party_id = party_name

    def __repr__(self) -> str:
        return f'<SurveyParties survey_party_id={self.survey_party_id}>'

    def json(self) -> dict:
        return {
            'survey_party_id': self.survey_party_id,
            'survey_id': self.survey_id,
            'party_name': self.party_name
        }