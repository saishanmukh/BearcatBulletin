from app.db import db


class Images(db.Model):
    __table__name = 'images'

    image_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    news_id = db.Column(db.Integer, db.ForeignKey('news.news_id'), nullable=False)
    image_path = db.Column(db.String(80), nullable=False)

    def __init__(self, news_id, image_path):
        self.news_id = news_id
        self.image_path = image_path

    def __repr__(self) -> str:
        return f'<Images image_id={self.image_id}>'  

    def json(self) -> dict:
        return {
            'image_id': self.image_id,
            'news_id': self.news_id,
            'image_path': self.image_path
        }

    @classmethod
    def find_by_id(cls, image_id: int) -> "Images":
        return cls.query.filter_by(image_id=image_id).first()
    
    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()