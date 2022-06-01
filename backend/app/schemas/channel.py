from  app.ma import ma
from marshmallow import pre_dump
from marshmallow import fields
from marshmallow import validate


from app.models.channel import Channel


class ChannelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Channel
        fields = ("channel_id", "channel_name", "admin_user_id")
        dump_only = ("channel_id", )

