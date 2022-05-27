from pyrsistent import optional
from sqlalchemy import desc
from app.ma import ma
from marshmallow import pre_dump
from marshmallow import fields
from marshmallow import validate
# from marshmallow.fields import String, Integer, DateTime, Nested
from app.models.news import News
from app.schemas.images import ImagesSchema

class NewsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = News
        fields = ("news_id", "headline", "description", "category", "hashtag", "posted_by", "channel_id", "posted_date", "edited_date")
        dump_only = ("news_id", )

class NewsSchemaWithImages(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = News
        fields = ("news_id", "description", "images")
        dump_only = ("news_id", )
    images = fields.List(fields.Nested(ImagesSchema, optional=True))