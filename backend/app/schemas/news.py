from sqlalchemy import desc
from app.ma import ma
from marshmallow import pre_dump
from marshmallow import fields
from marshmallow import validate
# from marshmallow.fields import String, Integer, DateTime, Nested
from app.models.news import News


class NewsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = News
        # load_instance = True
        fields = ("news_id", "headline", "description", "category", "hashtag", "posted_by", "channel", "posted_date", "edited_date")
        dump_only = ("news_id", )
