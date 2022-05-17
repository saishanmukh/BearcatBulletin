from sqlalchemy import desc
from app.ma import ma
from marshmallow import pre_dump
from marshmallow import fields
from marshmallow import validate


class OrderByFilterSchema(ma.Schema):
    order_by = fields.Str(
        missing=None,
        description='Order by field.',
        validate=validate.OneOf(['sis_id', 'name', 'email', 'created_at']),
        required=False)