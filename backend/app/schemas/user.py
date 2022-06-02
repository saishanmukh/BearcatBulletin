from sqlalchemy import desc
from app.ma import ma
from marshmallow import pre_dump
from marshmallow import fields
from marshmallow import validate
# from marshmallow.fields import String, Integer, DateTime, Nested
from app.models.user import User

PAGINATION_PAGE_VALUE_DEFAULT = 1
PAGINATION_PAGE_VALUE_MIN = 1
PAGINATION_PAGE_VALUE_MAX = 100
PAGINATION_PER_PAGE_VALUE_DEFAULT = 10
PAGINATION_PER_PAGE_VALUE_MIN = 1
PAGINATION_PER_PAGE_VALUE_MAX = 100



class RequestPathParamsSchema(ma.SQLAlchemyAutoSchema):
    pass

class RequestQueryParamsSchema(ma.SQLAlchemyAutoSchema):
    pass

class RequestBodyParamsSchema(ma.SQLAlchemyAutoSchema):
    pass

class PaginationQueryParamsSchema(RequestQueryParamsSchema):
    page = fields.Int(
        missing=PAGINATION_PAGE_VALUE_DEFAULT,
        description='Pagination page number, first page is 1.',
        validate=validate.Range(min=PAGINATION_PAGE_VALUE_MIN, max=PAGINATION_PAGE_VALUE_MAX),
        required=False)
    per_page = fields.Int(
        missing=PAGINATION_PER_PAGE_VALUE_DEFAULT,
        description='Pagination items per page.',
        validate=validate.Range(min=PAGINATION_PER_PAGE_VALUE_MIN, max=PAGINATION_PER_PAGE_VALUE_MAX),
        required=False)

class UsersRequestPathParamsSchema(RequestPathParamsSchema):
    city_id = fields.Int(
        description='The id of the city.',
        validate=validate.Range(min=1, max=9999),
        required=True)

class UsersCreateRequestBodyParamsSchema(RequestBodyParamsSchema):
    name = fields.Str(
        description='The name of the city',
        validate=validate.Length(min=2, max=40),
        required=True)

class UsersUpdateRequestBodyParamsSchema(RequestBodyParamsSchema):
    name = fields.Str(
        description='The name of the city',
        validate=validate.Length(min=2, max=40),
        required=True)



class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        ordered = True
        fields = ("id", "email", "first_name", "last_name", "role", "created_date", "password")
        dump_only = ("id", "created_date")
        load_only = ("password",)

    @pre_dump
    def pre_dump(self, data,  **kwargs):
        data.role = data.role.value
        return data

    def get_role(self, obj) -> str:
        return obj.role.value

class UserSchemaForSignup(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        ordered = True
        fields = ("id", "email", "first_name", "last_name", "role", )
        dump_only = ("id", )

    @pre_dump
    def pre_dump(self, data,  **kwargs):
        data.role = data.role.value
        return data

    def get_role(self, obj) -> str:
        return obj.role.value


class UserLoginSchema(ma.Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)

class UserSchemaForSignupWithToken(ma.Schema):
    email = fields.Str(required=True)
    otp_code = fields.Str(required=True)
    password = fields.Str(required=True)


class UserFilterQueryParamsSchema(UserSchema):
    def __init__(self, fields = [], required = []):
        super(UserFilterQueryParamsSchema, self).__init__()
        if len(fields) > 0:
            unwanted_fields = set(self.fields.keys())- set(fields)
            for field in unwanted_fields:
                self.fields.pop(field)

        for field in self.fields.keys():
            if field not in required:
                self.fields[field].required = False

class UserIncludeResponseSchema(UserSchema):
    def __init__(self, fields = [], required = []):
        super(UserIncludeResponseSchema, self).__init__()
        if len(fields) > 0:
            unwanted_fields = set(self.fields.keys())- set(fields)
            for field in unwanted_fields:
                self.fields.pop(field)
    class Meta:
        ordered = True

class NameFilterQueryParamsSchema(ma.SQLAlchemyAutoSchema):
    sis_id = fields.Str(
        description='The sis_id of the user',
        required=False)