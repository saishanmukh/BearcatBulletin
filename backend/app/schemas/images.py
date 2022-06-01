from sqlalchemy import desc
from app.ma import ma
from marshmallow import pre_dump
from marshmallow import fields
from marshmallow import validate
# from marshmallow.fields import String, Integer, DateTime, Nested
from app.models.images import Images


class ImagesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Images
        fields = ("image_id", "news_id", "image_path")
        dump_only = ("image_id", )